# -*- coding: utf-8 -*-

# scrapy genspider -t basic tmp example.com

import scrapy


class TmpSpider(scrapy.Spider):
    name = 'tmp'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/']

    def parse(self, response):
        # 可以自己写爬取路径和回调规则
        pass

    # 可以写多个解析函数，获取想要的数据
    def parse2(self, response):
        pass