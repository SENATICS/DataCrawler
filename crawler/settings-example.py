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
# Especificar aqui la ubicacion donde se levanta el servidor splash
SPLASH_URL = 'http://your_splash_location:8050/render.html?url='
# Especificar aqui la url del Catalogo
CATALOG_URL = 'http://your_catalog_site/api/3/action/'
# Especificar aqui la API Key del Catalago
API_KEY = "xxxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"

# DEPTH_LIMIT = 1

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'tutorial (+http://www.yourdomain.com)'
