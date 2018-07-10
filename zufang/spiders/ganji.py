# -*- coding: utf-8 -*-

# scrapy genspider ganji ganji.com

import scrapy


class GanjiSpider(scrapy.Spider):
    name = 'ganji'
    allowed_domains = ['ganji.com']
    start_urls = ['http://ganji.com/']

    def parse(self, response):
        pass
