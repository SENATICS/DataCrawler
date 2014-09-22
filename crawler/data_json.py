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
#----------------------------------------------------------------------------
# This file is part of the Governance and Democracy Program USAID-CEAMSO,
# is distributed as free software in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. You can redistribute it and/or modify it under the
# terms of the GNU Lesser General Public License version 2 as published by the
# Free Software Foundation, accessible from <http://www.gnu.org/licenses/> or write
# to Free Software Foundation (FSF) Inc., 51 Franklin St, Fifth Floor, Boston,
# MA 02111-1301, USA.
#---------------------------------------------------------------------------
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

from crawler import file_controller as FileController

try:
    import json
except ImportError:
    import simplejson as json


class DataJson:
    def convert(self, domain):
        """
        Parsea un archivo .json con los datos extraidos de una pagina anotada con microdata a un nuevo archivo data.json
        con el formato POD (Project Open Data).
        """
        response = []
        url_aux = "url"
        distribution_aux = "distribution"
        encoding_aux = "encodingFormat"
        file = domain + ".json"
        with open(file) as data_file:
            data = json.load(data_file)
            """ Iterar sonbre la lista de cada dominio """
            for item in data["root"]:
                """ Iterar sobre las propiedades de cada item """
                for properties in item["items"]:
                    tipo = properties["type"][0].encode("utf-8")

                    """ Si es del tipo Dataset """
                    if (tipo == 'http://schema.org/Dataset'):
                        property = properties["properties"]
                        """ Si tiene datos """
                        if property:
                            url = ""
                            if url_aux in property.keys():
                                url = property["url"][0]

                            """ Iterar sobre creator (publicador) """
                            for creator in property["creator"]:
                                creatorproperty = creator["properties"]

                            """ Iterar sobre provider (organizacion) """
                            for provider in property["provider"]:
                                providerproperty = provider["properties"]

                            distributionlist = []
                            if distribution_aux in property.keys():
                                for distribution in property["distribution"]:
                                    distributionproperty = distribution["properties"]
                                    # Si no tiene el encoding ni la url no guarda el recurso
                                    if encoding_aux in distributionproperty.keys() and url_aux in distributionproperty.keys():
                                        format = distributionproperty["encodingFormat"][0]
                                        accessURL = distributionproperty["url"][0]
                                        distributionobject = {'format': format, 'accessURL': accessURL}
                                        distributionlist.append(distributionobject)

                            keys_aux = property["keywords"][0]
                            keywords = keys_aux.split(",")
                            if not keys_aux:
                                keywords = []

                            """
                            Name cambia por title
                            Url cambia por uniqueid
                            Description se mantiene
                            Keywords cambia por keyword
                            Creator name cambia por contactProvider
                            Creator email cambia por mbox
                            Access level se pone public por defecto
                            Version se mantiene
                            License se mantiene
                            Temporal se mantiene
                            Falta spatial
                            Provider name cambia por publisher
                            """
                            response.append({'title': property["name"][0],
                                             'landingPage': url,
                                             'description': property["description"][0],
                                             'contactName': creatorproperty["name"][0],
                                             'mbox': creatorproperty["email"][0],
                                             'keyword': keywords,
                                             'accessLevel': "public",
                                             'version': property["version"][0],
                                             'license': property["license"][0],
                                             'temporal': property["temporal"][0],
                                             'publisher': providerproperty["name"][0],
                                             'distribution': distributionlist})

                    """ Si es del tipo DataCatalog """
                    if (tipo == 'http://schema.org/DataCatalog'):
                        property = properties["properties"]

                        """
                        Title es Data Catalog
                        Name
                        Url
                        Description
                        Debe tener los otros datos ??
                        """
                        keywords_catalog = ["catalog"]

                        response.append({'title': "Data Catalog",
                                         'landingPage': property["url"][0],
                                         'description': property["description"][0],
                                         'contactName': "",
                                         'mbox': "",
                                         'keyword': keywords_catalog,
                                         'accessLevel': "public",
                                         'publisher': ""})

                        """ Iterar sobre los datasets """
                        dataset_aux = "dataset"
                        if dataset_aux in property.keys():
                            print "Tiene datasets"
                            for dataset in property["dataset"]:
                                dataproperty = dataset["properties"]
                                url = ""
                                if url_aux in dataproperty.keys():
                                    url = dataproperty["url"][0]
                                """ Iterar sobre creator (publicador) """
                                for creator in dataproperty["creator"]:
                                    creatorproperty = creator["properties"]
                                """ Iterar sobre provider (organizacion) """
                                for provider in dataproperty["provider"]:
                                    providerproperty = provider["properties"]

                                distributionlist = []
                                if distribution_aux in property.keys():
                                    for distribution in property["distribution"]:
                                        distributionproperty = distribution["properties"]
                                        # Si no tiene el encoding ni la url no guarda el recurso
                                        if encoding_aux in distributionproperty.keys() and url_aux in distributionproperty.keys():
                                            format = distributionproperty["encodingFormat"][0]
                                            accessURL = distributionproperty["url"][0]
                                            distributionobject = {'format': format, 'accessURL': accessURL}
                                            distributionlist.append(distributionobject)

                                keys_aux = dataproperty["keywords"][0]
                                keywords = keys_aux.split(",")
                                if not keys_aux:
				                    keywords = []

                                response.append({'title': dataproperty["name"][0],
                                                 'landingPage': url,
                                                 'description': dataproperty["description"][0],
                                                 'contactName': creatorproperty["name"][0],
                                                 'mbox': creatorproperty["email"][0],
                                                 'keyword': keywords,
                                                 'accessLevel': "public",
                                                 'version': dataproperty["version"][0],
                                                 'license': dataproperty["license"][0],
                                                 'temporal': dataproperty["temporal"][0],
                                                 'publisher': providerproperty["name"][0],
                                                 'distribution': distributionlist})
        """ Escribe en el archivo final """
        filename = FileController.FileController().save_existing_data_json(response, domain, False)
        """ Elimina el archivo temporal de items """
        FileController.FileController().clean_item_tmp_file(domain)

        return filename

# DataJson().convert("datos.mec.gov.py")
