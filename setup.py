__author__ = 'desa2'

from setuptools import setup, find_packages

setup(
    name         = 'datacrawler',
    version      = '1.0',
    packages     = find_packages(),
    entry_points = {'scrapy': ['settings = crawler.settings']},
    scripts = ['bin/Test.py'],
    install_requires=[
          'lxml', 'scrapy', 'ipython', 'click', 'service_identity==1.0.0', 'requests', 'microdata==0.5'
    ],
)
