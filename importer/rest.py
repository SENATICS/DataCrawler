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

import json
import requests
import datetime
import os
import sys
from zipfile import ZipFile
from scrapy.utils.project import get_project_settings
from model import DataEntry, CkanDataset
from scrapy import log, signals


class CKANImporter(object):
    def __init__(self):
        settings = get_project_settings()
        self.headers = {'Authorization': settings['API_KEY'], 'Content-type': 'application/json'}
        self.base_url = settings['CATALOG_URL']

    def import_package(self, filename, modalidad):
        with open(filename) as file:  # Use file to refer to the file object
            base_dir = '/'.join(filename.split('/')[0:-1]) + '/'
            data = file.read()
            entries = [DataEntry(**j) for j in json.loads(data)]
            datasets = [CkanDataset(e, modalidad) for e in entries]
            valid = [d for d in datasets if d.resources]
            old_datasets = []
            try:
                for d in valid:
                    r = self.create_or_update_dataset(d)
                    if r:
                        old_datasets.append(r)
            finally:
                if old_datasets:
                    dt = str(datetime.datetime.now())
                    filename = 'backup ' + dt
                    with open(base_dir + filename + '.txt', 'a') as f:
                        f.write(json.dumps(old_datasets))
                        with ZipFile(base_dir + filename + '.zip', 'w') as myzip:
                            myzip.write(base_dir + filename + '.txt')

                    if os.path.isfile(base_dir + filename + '.txt'):
                        os.remove(base_dir + filename + '.txt')


    def create_or_update_dataset(self, dataset):
        dataset.owner_org = self.get_organization_id(dataset.owner_org)
        r = None
        exists, old = self.dataset_exists(dataset.name)
        confirm = ''
        if exists:
            print old
            while not confirm in ['s', 'n']:
                confirm = raw_input("El dataset ya existe. Desea actualizarlo con los valores anteriores? (s/n) ")
            if confirm == 's':
                r = self.update_dataset(dataset, old)
                print 'Se ha actualizado el dataset %s' % dataset.name
                return old
        else:
            print dataset
            while not confirm in ['s', 'n']:
                confirm = raw_input("Desea crear un nuevo dataset con los valores anteriores? (s/n) ")
            if confirm == 's':
                r = self.create_dataset(dataset)
                print 'Se ha creado el dataset %s' % dataset.name

    def create_dataset(self, dataset):
        url = self.base_url + 'package_create'
        dataset_dict = dataset.as_dict()
        r = requests.post(url, data=json.dumps(dataset_dict), headers=self.headers)
        if r.status_code == 200:
            return r


    def update_dataset(self, dataset, current):
        url = self.base_url + 'package_update'
        dataset_dict = dataset.as_dict()
        merge_dict = self.merge_datasets(dataset_dict, current)
        r = requests.post(url, data=json.dumps(merge_dict), headers=self.headers)
        if r.status_code == 200:
            return r

    def merge_datasets(self, a, b):
        for key in a.keys():
            b[key] = a[key]
        return b

    def dataset_exists(self, name):
        url = self.base_url + 'package_show'
        params = {'id': name}
        r = requests.get(url, headers=self.headers, params=params)
        log.msg(r.status_code, level=log.DEBUG)
        return (r.status_code == 200, r.json().get('result'))

    def get_organization_id(self, org_name):
        url = self.base_url + 'organization_show'
        params = {'id': org_name}
        r = requests.get(url, params=params)
        return r.json().get('result')['id']


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding("utf-8")
    importer = CKANImporter()
    # Para pruebas sin ejecutar el crawler
    importer.import_package('/home/desa2/PycharmProjects/DataCrawler/bin/results_17_09_14/datos.mec.gov.py/data.json',
                            'data-hunting')
