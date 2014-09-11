__author__ = 'Verena Ojeda'

import requests
import click
from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy import log, signals
from scrapy.utils.project import get_project_settings
from crawler.spiders import data_spider
from crawler.spiders.data_spider import DataSpider
from crawler import data_json as DataJson
from crawler import file_controller as FileController


@click.command()
@click.option('--file',  # prompt='Path to your file with domains to crawl',
              default="/home/desa2/PycharmProjects/DataCrawler/crawler/domains.txt",
              help='The list of domains to crawl.')
def main(file):
    click.echo('File path: %s' % file)
    call_spider(file)


def call_spider(file):
    """
    Crea el spider y ejecuta el reactor. Copia los resultados del crawling a los archivos .json para luego
    transformarlos a los archivos data.json correspondientes.
    """
    with open(file, "r") as f:
        list_url = f.readlines()
        domains = []
        urls = []
        for u in list_url:
            domain = u.strip('\n')
            url = "http://" + u.strip('\n') + "" + "/"
            print "============= Domain " + domain
            print "============= Start url " + url
            response = requests.get(url + "/data.json")
            if response.status_code == 200:
                FileController.FileController().save_existing_data_json(response, domain, True)
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
        #FileController.FileController().clean_tmp_files()

        """ Convertir los archivos .json a data.json (formato POD) """
        for domain in domains:
            DataJson.DataJson().convert(domain)


results = []


def spider_closed(spider):
    print results


if __name__ == '__main__':
    main()