# -*- coding: utf-8 -*-
#
# @author	Rodrigo Parra
# @copyright	2014 Governance and Democracy Program USAID-CEAMSO
# @license 	http://www.gnu.org/licenses/gpl-2.0.html
#
# USAID-CEAMSO
# Copyright (C) 2014 Governance and Democracy Program
# http://ceamso.org.py/es/proyectos/20-programa-de-democracia-y-gobernabilidad
#
# ----------------------------------------------------------------------------
# This file is part of the Governance and Democracy Program USAID-CEAMSO,
# is distributed as free software in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. You can redistribute it and/or modify it under the
# terms of the GNU Lesser General Public License version 2 as published by the
# Free Software Foundation, accessible from <http://www.gnu.org/licenses/> or write
# to Free Software Foundation (FSF) Inc., 51 Franklin St, Fifth Floor, Boston,
# MA 02111-1301, USA.
# ---------------------------------------------------------------------------
# Este archivo es parte del Programa de Democracia y Gobernabilidad USAID-CEAMSO,
# es distribuido como software libre con la esperanza que sea de utilidad,
# pero sin NINGUNA GARANTÍA; sin garantía alguna implícita de ADECUACION a cualquier
# MERCADO o APLICACION EN PARTICULAR. Usted puede redistribuirlo y/o modificarlo
# bajo los términos de la GNU Lesser General Public Licence versión 2 de la Free
# Software Foundation, accesible en <http://www.gnu.org/licenses/> o escriba a la
# Free Software Foundation (FSF) Inc., 51 Franklin St, Fifth Floor, Boston,
# MA 02111-1301, USA.
#
__author__ = 'Rodrigo Parra'

import requests
import click
import sys
import os
import time
import signal
import subprocess
from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy import log, signals
from scrapy.utils.project import get_project_settings
from crawler.spiders import data_spider
from crawler.spiders.data_spider import DataSpider
from crawler import data_json as DataJson
from crawler import file_controller as FileController

from importer.rest import CKANImporter


@click.command()
@click.option('--file',  # prompt='Path to your file with domains to crawl',
              default="/home/desa2/PycharmProjects/DataCrawler/crawler/domains.txt",
              help='The list of domains to crawl.')
@click.option('--virtualenv',  # prompt='Path to your virtual enviroment',
              default="/home/desa2/datos",
              help='The path of the virtual enviroment.')
def main(file, virtualenv):
    # Iniciar splash
    pro = subprocess.Popen('./run_splash.sh ' + virtualenv, stdout=subprocess.PIPE,
                           shell=True, preexec_fn=os.setsid)
    time.sleep(10)
    click.echo('File path: %s' % file)
    created_files = call_spider(file)
    #import_to_ckan(created_files)
    # Finalizar splash
    os.killpg(pro.pid, signal.SIGTERM)


def call_spider(file):
    """
    Crea el spider y ejecuta el reactor. Copia los resultados del crawling a los archivos .json para luego
    transformarlos a los archivos data.json correspondientes.
    """
    with open(file, "r") as f:
        list_url = f.readlines()
        domains = []
        urls = []
        created_files = []
        for u in list_url:
            domain = u.strip('\n')
            url_aux = domain.split("/")
            domain_type = False
            if (len(url_aux) > 1):
                domain = url_aux[0]
                url = "http://" + url_aux[0] + "/datos"
            else:
                url = "http://" + u.strip('\n') + ""
                domain_type = True
            print "============= Domain " + domain
            print "============= Start url " + url
            response = requests.get(url + "/data.json")
            if response.status_code == 200:
                filename = FileController.FileController().save_existing_data_json(response, domain, True)
                created_files.append({'modalidad': 'recolecta', 'archivo': filename})
            else:
                domains.append(domain)
                urls.append(url)

        spider = DataSpider(domains=domains, start_urls=urls, domain_type=domain_type)
        settings = get_project_settings()
        crawler = Crawler(settings)
        crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
        crawler.configure()
        crawler.crawl(spider)
        crawler.start()
        log.start(logfile="log.txt", loglevel=log.DEBUG, logstdout=False)
        reactor.run()  # the script will block here

        """ Copiar los datos a los archivos .json """
        data_spider.copy_items_to_files()

        """ Eliminar archivos temporales """
        FileController.FileController().clean_tmp_files()

        """ Convertir los archivos .json a data.json (formato POD) """
        for domain in domains:
            filename = DataJson.DataJson().convert(domain)
            created_files.append({'modalidad': 'data-hunting', 'archivo': filename})

        return created_files


results = []


def spider_closed(spider):
    print results


def import_to_ckan(created_files):
    importer = CKANImporter()
    for f in created_files:
        m = 'Importing %s' % str(f)
        log.msg(m, level=log.DEBUG)
        importer.import_package(f['archivo'], f['modalidad'])
        log.msg("Paso el importer", level=log.DEBUG)


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding("utf-8")
    main()
