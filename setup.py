__author__ = 'Verena Ojeda'

from setuptools import setup, find_packages

setup(
    name         = 'datacrawler',
    version      = '1.0',
    packages     = find_packages(),
    entry_points = {'scrapy': ['settings = crawler.settings']},
    scripts = ['bin/DataCrawler.py'],
    install_requires=[
          'lxml', 'scrapy', 'ipython', 'click', 'service_identity==1.0.0', 'requests', 'microdata==0.5',
          'qt4reactor', 'psutil', 'adbockparser', 'Pillow'
    ],
)
