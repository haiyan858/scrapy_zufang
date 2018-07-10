# -*- coding: utf-8 -*-

# CrawlSpider 和 spider 的差异
# scrapy genspider -t crawl ganji2 ganji.com

# CrawlSpider的优点
# 1、爬取有规律的网站
# 比如用户的关注数量，简书的文章数量等

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class Ganji2Spider(CrawlSpider):
    name = 'ganji2'
    allowed_domains = ['ganji.com']
    start_urls = ['http://bj.ganji.com/fang1/']

    get_links = []

    # 3、分析页面中所有的链接，拿到符合正则匹配的链接，跳到对应的函数中
    # 匹配路由
    rules = (
        Rule(LinkExtractor(allow=r'http://bj.ganji.com/fang1/\d+x.htm'), callback='parse_item', follow=False),
        Rule(LinkExtractor(allow=r'http://bj.ganji.com/fang1/o\d+'), callback='', follow=False),
    )

    # 2、parse函数不能被重写，如果重写可能会导致整个爬虫不工作，异常
    # def parse(self, response):
    #     pass

    # 4、负责解析数据
    def parse_item(self, response):
        i = {}

        # self.get_links.append(response)
        # print(response.url,len(self.get_links))

        i['title'] = response.xpath('//p[@class="card-title"]/i/text()').extract()
        i['money'] = response.xpath('//span[@class="num"]/text()').extract()
        i['payway'] = response.xpath('//ul[@class="card-pay f-clear"]/li[@class="type"]/text()').extract()
        i['house_type'] = response.xpath('//li[@class="item f-fl"]/span[@class="content"]/text()').extract()[0]
        i['area'] = response.xpath('//li[@class="item f-fl"]/span[@class="content"]/text()').extract()[1]
        i['orientation'] = response.xpath('//li[@class="item f-fl"]/span[@class="content"]/text()').extract()[2]
        i['floor'] = response.xpath('//li[@class="item f-fl"]/span[@class="content"]/text()').extract()[3]
        i['elevator'] = response.xpath('//li[@class="item f-fl"]/span[@class="content"]/text()').extract()[4]
        i['finish'] = response.xpath('//li[@class="item f-fl"]/span[@class="content"]/text()').extract()[5]
        i['address'] = response.xpath('//li[@class="er-item f-fl"][2]/span[@class="content"]/a/text()').extract()

        print(i)

        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i
