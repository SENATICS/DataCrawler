# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class DataItem(scrapy.Item):
    title = scrapy.Field()
    links = scrapy.Field()
    visit_id = scrapy.Field()
    visit_status = scrapy.Field()