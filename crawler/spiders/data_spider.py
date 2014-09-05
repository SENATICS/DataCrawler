import requests

__author__ = 'desa2'

import time
import urllib
import rdflib

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.utils.project import get_project_settings
from microdata import get_items
from crawler.items import DataItem
from rdflib.serializer import Serializer

try:
    import json
except ImportError:
    import simplejson as json

""" Registra el serializador microdata para la libreria rdflib """
rdflib.plugin.register("microdata", Serializer, "rdflib.plugins.serializers.microdata", "MicrodataSerializer")

known_vocabs = {
    "eco": "http://www.ebusiness-unibw.org/ontologies/eclass/5.1.4/#",
    "owl": "http://www.w3.org/2002/07/owl#",
    "dbpedia": "http://dbpedia.org/resource/",
    "dc": "http://purl.org/dc/elements/1.1/",
    "dcterms": "http://purl.org/dc/terms/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "gr": "http://purl.org/goodrelations/v1#",
    "foaf": "http://xmlns.com/foaf/0.1/",
    "vcard": "http://www.w3.org/2006/vcard/ns#",
    "vso": "http://purl.org/vso/ns#",
    "tio": "http://purl.org/tio/ns#",
    "coo": "http://purl.org/coo/ns#",
    "vvo": "http://purl.org/vvo/ns#",
    "fab": "http://purl.org/fab/ns#",
    "xro": "http://purl.org/xro/ns#",
    "xhv": "http://www.w3.org/1999/xhtml/vocab#",
    "schema": "http://schema.org/",
    "grddl": "http://www.w3.org/2003/g/data-view#",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "rdfa": "http://www.w3.org/ns/rdfa#",
    "rif": "http://www.w3.org/2007/rif#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "skosxl": "http://www.w3.org/2008/05/skos-xl#",
    "wdr": "http://www.w3.org/2007/05/powder#",
    "void": "http://rdfs.org/ns/void#",
    "wdsr": "http://www.w3.org/2007/05/powder-s#",
    "xml": "http://www.w3.org/XML/1998/namespace",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "cc": "http://creativecommons.org/ns#",
    "ctag": "http://commontag.org/ns#",
    "ical": "http://www.w3.org/2002/12/cal/icaltzd#",
    "og": "http://ogp.me/ns#",
    "rev": "http://purl.org/stuff/rev#",
    "sioc": "http://rdfs.org/sioc/ns#",
    "v": "http://rdf.data-vocabulary.org/#",
    "dv": "http://data-vocabulary.org/"
}

items_list = []


class DataSpider(CrawlSpider):
    name = "dspider"
    # allowed_domains = ["mec.gov.py"]
    # start_urls = [
    # "http://datos.mec.gov.py/",
    # ]
    settings = get_project_settings()
    rules = [
        Rule(SgmlLinkExtractor(allow=settings['ALLOW_FILTER'], deny=settings['DENY_FILTER']), callback='parse_item',
             follow=True)]
    ITEM_PIPELINES = [
        'tutorial.pipelines.JsonWriterPipeline'
    ]


    def __init__(self, domains, start_urls, *args, **kwargs):
        self.start_urls = start_urls
        self.allowed_domains = domains
        super(DataSpider, self).__init__(*args, **kwargs)
        self._compile_rules()  # ?


    def __del__(self):
        CrawlSpider.__del__(self)


    def parse_item(self, response):
        self.log('A response from %s just arrived!' % response.url)
        time.sleep(3)
        # item = DataItem()
        # item['title'] = response.xpath('//title/text()').extract()
        # links = response.xpath('//a[contains(@href, "/")]')
        # item['links'] = links.extract()
        transformar(response.url)
        # yield item


def transformar(url):
    """ Si la pagina esta anotada con rdfa, primero se transforma a microdata y luego se guarda en un archivo .html
    para que luego pueda ser leido. Esta seccion todavia se encuentra en su version de prueba. """

    microdata = {}
    microdata['items'] = items = []

    url_splash = "http://192.168.0.21:8050/render.html?url=" + url + "&timeout=20&wait=2.5"
    file_splash = open('splash.html', 'w')
    html = urllib.urlopen(url_splash)
    file_splash.write(str(html.read()))
    url_final = "splash.html"

    # serialization = requests.get("http://rdf-translator.appspot.com/convert/rdfa/microdata/html/" + url)
    serialization = rdfa_to_microdata(url_splash)
    if serialization:
        file = open('aux.html', 'wb')
        file.write(serialization.encode('utf-8'))
        url_final = "aux.html"

    items = get_items(urllib.urlopen(url_final))
    # Para solucionar el problema de que viene mas de un item nomas, esto deberia arreglarse
    if len(items) > 1:
        indice = 1
    else:
        indice = 0
    # Si tiene atributos se agrega o modifca en la lista
    if items:
        if items[indice].props:
            refresh_items_list(items[indice])


def refresh_items_list(item_nuevo):
    # OJO: se tiene que pasar siempre -1, estas anotaciones hay que arreglar
    add_item = True

    # Itera sobre la lista de items existentes
    for item in items_list:
        add_item = True
        # Si el item a comparar es DataCatalog
        if item.itemtype == "[http://schema.org/Datacatalog]":

            # Si el nuevo item es DataCatalog compara directo
            if item.itemtype == item_nuevo.itemtype:

                # Si ya existe modifica
                if item.props['url'] == item_nuevo.props['url']:
                    add_item = False

                    # Agrega los nuevos atributos del item
                    for name, values in item_nuevo.props.items():
                        if not item.props[name]:
                            for v in values:
                                item.props[name].append(v)

            # Si el nuevo item es DataSet busca entre sus datasets
            else:
                for datasets in item.get_all('datasets'):
                    for dataset in datasets:

                        # Si el item ya existe modifica
                        if dataset.props['url'] == item_nuevo.props['url']:
                            add_item = False

                            # Agrega los nuevos atributos del item
                            for name, values in item_nuevo.props.items():
                                if not dataset.props[name]:
                                    for v in values:
                                        dataset.props[name].append(v)

        # Si el item a comparar es DataSet (todavia no se puede porque no esta anotada la url)
        else:
            add_item = True
            # Si el item ya existe modifica
            """if item.props['url'] == item_nuevo.props['url']:
                addItem = False

                # Agrega los nuevos atributos del item
                for name, values in item_nuevo.props.items():
                    if not item.props[name]:
                        for v in values:
                            item.props[name].append(v)"""

    # Si es un nuevo item agrega a la lista
    if add_item:
        items_list.append(item_nuevo)


def copy_items_to_file(file_name):
    file = open(file_name, 'ab+')
    file.write('{ "root": [')
    for item in items_list:
        file.write(str("{\"items\": [" + item.json() + "]},"))
    file.seek(0, 2)
    file.seek(file.tell() - 1, 0)
    val = file.read()
    print val
    if (val == ','):
        file.truncate(file.tell() - 1)
    file.write(']}')
    file.close()


""" Version de prueba para transformar paginas anotadas con rdfa a mircrodata """


def rdfa_to_microdata(url):
    global known_vocabs
    target_format = "microdata"
    source_format = "rdfa"
    base = "http://rdf-translator.appspot.com/"
    prefixes = known_vocabs
    g = rdflib.Graph()

    for key, value in dict.items(prefixes):
        g.bind(key, value, override=True)

    g.parse(url, format=source_format, publicID=base)

    if len(g) > 0:
        serialization = g.serialize(format=target_format).decode("UTF-8")
        return serialization
    else:
        return ""