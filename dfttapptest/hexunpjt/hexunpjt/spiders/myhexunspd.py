# -*- coding: utf-8 -*-
import scrapy


class MyhexunspdSpider(scrapy.Spider):
    name = "myhexunspd"
    allowed_domains = ["hexun.com"]
    start_urls = ['http://hexun.com/']

    def parse(self, response):
        pass
