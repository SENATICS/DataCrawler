__author__ = 'Verena Ojeda'

import scrapy

class DataItem(scrapy.Item):
    title = scrapy.Field()
    links = scrapy.Field()
    visit_id = scrapy.Field()
    visit_status = scrapy.Field()