# -*- coding: utf-8 -*-

BOT_NAME = 'crawler'

SPIDER_MODULES = ['crawler.spiders']
NEWSPIDER_MODULE = 'crawler.spiders'
DUPEFILTER_CLASS = 'scrapy.dupefilter.RFPDupeFilter'
ALLOW_FILTER = ('\.htm', '\.html', '/')
DENY_FILTER = ('\.pdf', '\.zip')
LOG_LEVEL = 'INFO'
COOKIES_ENABLED = False
LOG_FILE = 'datacrowler.log'
SPLASH_URL = 'http://192.168.0.21:8050/render.html?url='
#DEPTH_LIMIT = 1 

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'
