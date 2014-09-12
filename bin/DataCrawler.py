__author__ = 'Verena Ojeda'

import requests
import click
import sys
import os
import time
from multiprocessing import Process
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
def main(file):
    # Iniciar splash
    # p = Process(target=start_splash_server)
    # p.start()
    # time.sleep(10)
    click.echo('File path: %s' % file)
    created_files = call_spider(file)
    # Finalizar splash
    # p.terminate()
    import_to_ckan(created_files)


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
            url = "http://" + u.strip('\n') + "" + "/"
            print "============= Domain " + domain
            print "============= Start url " + url
            response = requests.get(url + "/data.json")
            if response.status_code == 200:
                filename = FileController.FileController().save_existing_data_json(response, domain, True)
                created_files.append({'modalidad': 'recolecta', 'archivo': filename})
            else:
                domains.append(domain)
                urls.append(url)

        spider = DataSpider(domains=domains, start_urls=urls)
        settings = get_project_settings()
        # settings.overrides['FEED_FORMAT'] = 'json'
        # settings.overrides['FEED_URI'] = 'result.json'
        crawler = Crawler(settings)
        crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
        crawler.configure()
        crawler.crawl(spider)
        crawler.start()
        log.start(loglevel=log.DEBUG)
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

def start_splash_server():
    # Inciar splash
    os.system("chmod +x run_splash.sh")
    os.system("./run_splash.sh /home/desa2/datos")


results = []


def spider_closed(spider):
    print results

def import_to_ckan(created_files):
    importer = CKANImporter()
    for f in created_files:
        m = 'Importing %s' % str(f)
        log.msg(m, level=log.DEBUG)
        importer.import_package(f['archivo'], f['modalidad'])


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding("utf-8")
    main()
