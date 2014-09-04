__author__ = 'desa2'

try:
    import json
except ImportError:
    import simplejson as json


class DataJson:
    def convert(self, file):
        response = []
        with open(file) as data_file:
            data = json.load(data_file)
            #print data.keys()
            """ Iterar sonbre la lista de cada dominio """
            for item in data["root"]:
                #print item.keys()
                """ Iterar sobre las propiedades de cada item """
                for properties in item["items"]:
                    tipo = properties["type"][0].encode("utf-8")

                    """ Si es del tipo Dataset """
                    if (tipo == 'http://schema.org/Dataset'):
                        property = properties["properties"]
                        #print property.keys()
                        """ Si tiene datos """
                        if property:
                            # print("Name", property["name"][0].encode("utf-8"))
                            # print("Url", property["url"][0].encode("utf-8"))
                            # print("Description", property["description"][0].encode("utf-8"))

                            url = ""
                            urlAux = "url"
                            if urlAux in property.keys():
                                url = dataproperty["url"][0]
                                print("Url", dataproperty["url"][0].encode('utf-8'))

                            """ Iterar sobre creator (publicador) """
                            for creator in property["creator"]:
                                creatorproperty = creator["properties"]

                            """ Iterar sobre provider (organizacion) """
                            for provider in property["provider"]:
                                providerproperty = provider["properties"]

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
                                             'uniqueid': url,
                                             'description': property["description"][0],
                                             'contactName': creatorproperty["name"][0],
                                             'mbox': creatorproperty["email"][0],
                                             'keywords': property["keywords"],
                                             'accessLevel': "public",
                                             'version': property["version"][0],
                                             'license': property["license"][0],
                                             'temporal': property["temporal"][0],
                                             'publisher': providerproperty["name"][0]})

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
                        response.append({'title': "Data Catalog",
                                         'url': property["url"][0],
                                         'name': property["name"][0],
                                         'description': property["description"][0]})

                        """ Iterar sobre los datasets """
                        for dataset in property["dataset"]:
                            dataproperty = dataset["properties"]
                            #print dataproperty.keys()
                            url = ""
                            urlAux = "url"
                            if urlAux in dataproperty.keys():
                                url = dataproperty["url"][0]
                                print("Url", dataproperty["url"][0].encode('utf-8'))

                            """ Iterar sobre creator (publicador) """
                            for creator in dataproperty["creator"]:
                                creatorproperty = creator["properties"]

                            """ Iterar sobre provider (organizacion) """
                            for provider in dataproperty["provider"]:
                                providerproperty = provider["properties"]

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
                                                 'uniqueid': url,
                                                 'description': dataproperty["description"][0],
                                                 'contactName': creatorproperty["name"][0],
                                                 'mbox': creatorproperty["email"][0],
                                                 'keywords': dataproperty["keywords"],
                                                 'accessLevel': "public",
                                                 'version': dataproperty["version"][0],
                                                 'license': dataproperty["license"][0],
                                                 'temporal': dataproperty["temporal"][0],
                                                 'publisher': providerproperty["name"][0]})
        print response
        fileResponse = open('data.json', 'wb')
        fileResponse.write(json.dumps(response, indent=2))


#DataJson().convert("/home/desa2/PycharmProjects/DataCrawler/bin/items.json")