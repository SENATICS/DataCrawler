from crawler import DataJson
from crawler.spiders import data_spider

__author__ = 'desa2'

import click
from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy import log, signals
from scrapy.utils.project import get_project_settings
from crawler.spiders.data_spider import DataSpider


@click.command()
@click.option('--file', default="/home/desa2/PycharmProjects/DataCrawler/crawler/urls.txt",
              help='The list of urls to crawl.')
def main(file):
    click.echo('Hello %s!' % file)
    call_spider(file)


def call_spider(file):
    with open(file, "r") as f:
        list_url = f.readlines()
        domains = []
        urls = []
        for url in list_url:
            domain = url
            urlFinal = "http://" + url.strip('\n') + "/"
            print "============= Domain " + domain
            print "============= Url semilla " + urlFinal
            domains.append(domain)
            urls.append(urlFinal)

        spider = DataSpider(domain=domains, start_url=urls)
        settings = get_project_settings()
        #settings.overrides['FEED_FORMAT'] = 'json'
        #settings.overrides['FEED_URI'] = 'result.json'
        crawler = Crawler(settings)
        crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
        crawler.configure()
        crawler.crawl(spider)
        crawler.start()
        log.start(loglevel=log.DEBUG)
        reactor.run()  # the script will block here

        """ Copiar los datos al archivo final """
        data_spider.copy_items_to_file()
        file_items = open('items.json', 'ab+')
        file_items.seek(0,2)
        file_items.seek(file_items.tell()-1,0)
        val = file_items.read()
        print val
        if (val == ','):
            file_items.truncate(file_items.tell()-1)
        file_items.write(']}')
        file_items.close()

        """ Convertir el json extraido al json con formato POD """
        DataJson.DataJson().convert("items.json", domain)

        #""" Completar el archivo html """
        #fileHTML = open('resources.html', 'ab')
        #htmlFinal = """</ul></body>
    #</html>"""
        #fileHTML.write(htmlFinal)
        #fileHTML.close()


results = []


def spider_closed(spider):
    print results


if __name__ == '__main__':
    main()