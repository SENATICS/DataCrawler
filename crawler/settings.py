# -*- coding: utf-8 -*-

# Scrapy settings for tutorial project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
# http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'crawler'

SPIDER_MODULES = ['crawler.spiders']
NEWSPIDER_MODULE = 'crawler.spiders'
DUPEFILTER_CLASS = 'scrapy.dupefilter.RFPDupeFilter'
ALLOW_FILTER = ('\.htm', '\.html', '/')
DENY_FILTER = ('\.pdf', '\.zip')
#ONCURRENT_REQUESTS = 100
LOG_LEVEL = 'INFO'
COOKIES_ENABLED = False
#RETRY_ENABLED = False
#DOWNLOAD_TIMEOUT = 25
#REDIRECT_ENABLED = False
#MYEXT_ENABLED = True
#MYEXT_ITEMCOUNT = 1
LOG_FILE = 'datacrowler.log'
#DEPTH_LIMIT = 10
#EXTENSIONS = ['crawler.SpiderLogging']

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'
