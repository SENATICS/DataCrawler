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
        for u in list_url:
            domain = u.strip('\n')
            url = "http://" + u.strip('\n') + "/"
            print "============= Domain " + domain
            print "============= Url semilla " + url
            domains.append(domain)
            urls.append(url)

        spider = DataSpider(domains=domains, start_urls=urls)
        settings = get_project_settings()
        # settings.overrides['FEED_FORMAT'] = 'json'
        #settings.overrides['FEED_URI'] = 'result.json'
        crawler = Crawler(settings)
        crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
        crawler.configure()
        crawler.crawl(spider)
        crawler.start()
        log.start(loglevel=log.DEBUG)
        reactor.run()  # the script will block here

        """ Copiar los datos a los archivos finales """
        data_spider.copy_items_to_files()

        """ Convertir los archivos json extraidos a json con formato POD """
        for domain in domains:
            DataJson.DataJson().convert(domain)


results = []


def spider_closed(spider):
    print results


if __name__ == '__main__':
    main()