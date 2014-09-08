__author__ = 'desa2'

try:
    import json
except ImportError:
    import simplejson as json


class DataJson:
    def convert(self, domain):
        response = []
        urlAux = "url"
        distributionAux = "distribution"
        encodingAux = "encodingFormat"
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
                            if urlAux in property.keys():
                                url = dataproperty["url"][0]

                            """ Iterar sobre creator (publicador) """
                            for creator in property["creator"]:
                                creatorproperty = creator["properties"]

                            """ Iterar sobre provider (organizacion) """
                            for provider in property["provider"]:
                                providerproperty = provider["properties"]

                            distributionlist = []
                            if distributionAux in property.keys():
                                for distribution in property["distribution"]:
                                    distributionproperty = distribution["properties"]
                                    # Si no tiene el encoding ni la url no guarda el recurso
                                    if encodingAux in distributionproperty.keys() and urlAux in distributionproperty.keys():
                                        format = distributionproperty["encodingFormat"][0]
                                        accessURL = distributionproperty["url"][0]
                                        distributionobject = {'format': format, 'accessURL': accessURL}
                                        distributionlist.append(distributionobject)

                            """
                            Name cambia por title
                            Url cambia por uniqueid
                            Description se mantiene
                            Keywords se mantiene
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
                                             'keywords': property["keywords"],
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
                        keywords = ["catalog"]

                        response.append({'title': "Data Catalog",
                                         'landingPage': property["url"][0],
                                         'description': property["description"][0],
                                         'contactName': "",
                                         'mbox': "",
                                         'keywords': keywords,
                                         'accessLevel': "public",
                                         'publisher': ""})

                        """ Iterar sobre los datasets """
                        for dataset in property["dataset"]:
                            dataproperty = dataset["properties"]
                            url = ""
                            if urlAux in dataproperty.keys():
                                url = dataproperty["url"][0]

                            """ Iterar sobre creator (publicador) """
                            for creator in dataproperty["creator"]:
                                creatorproperty = creator["properties"]

                            """ Iterar sobre provider (organizacion) """
                            for provider in dataproperty["provider"]:
                                providerproperty = provider["properties"]

                            distributionlist = []
                            if distributionAux in property.keys():
                                for distribution in property["distribution"]:
                                    distributionproperty = distribution["properties"]
                                    # Si no tiene el encoding ni la url no guarda el recurso
                                    if encodingAux in distributionproperty.keys() and urlAux in distributionproperty.keys():
                                        format = distributionproperty["encodingFormat"][0]
                                        accessURL = distributionproperty["url"][0]
                                        distributionobject = {'format': format, 'accessURL': accessURL}
                                        distributionlist.append(distributionobject)

                            # Puede que necesite un tab
                            """
                            Name cambia por title
                            Url cambia por uniqueid
                            Description se mantiene
                            Keywords se mantiene
                            Creator name cambia por contactProvider
                            Creator email cambia por mbox
                            Access level se pone public por defecto
                            Version se mantiene
                            License se mantiene
                            Temporal se mantiene
                            Falta spatial
                            Provider name cambia por publisher
                            """
                            response.append({'title': dataproperty["name"][0],
                                             'landingPage': url,
                                             'description': dataproperty["description"][0],
                                             'contactName': creatorproperty["name"][0],
                                             'mbox': creatorproperty["email"][0],
                                             'keywords': dataproperty["keywords"],
                                             'accessLevel': "public",
                                             'version': dataproperty["version"][0],
                                             'license': dataproperty["license"][0],
                                             'temporal': dataproperty["temporal"][0],
                                             'publisher': providerproperty["name"][0],
                                             'distribution': distributionlist})
        print response
        fileResponse = open(domain + "_data.json", 'wb')
        fileResponse.write(json.dumps(response, indent=2))


        # DataJson().convert("/home/desa2/PycharmProjects/DataCrawler/bin/datos.mec.gov.py.json", "datos.mec.gov.py")