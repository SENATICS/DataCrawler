__author__ = 'verena'

from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy import log, signals
from scrapy.utils.project import get_project_settings

class ReactorControl:

    def __init__(self):
        self.crawlers_running = 0

    def add_crawler(self):
        self.crawlers_running += 1

    def remove_crawler(self):
        self.crawlers_running -= 1
        if self.crawlers_running == 0 :
            reactor.stop()

reactor_control = ReactorControl()
#log.start()