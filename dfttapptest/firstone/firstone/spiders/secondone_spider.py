#encoding=utf-8
import scrapy
import requests
from ..items import FirstoneItem
from scrapy.spiders import CrawlSpider,Rule,Request
from scrapy.spiders import Spider
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.http import Request

class MaimaiSpider(Spider):
    name = "lianhe1"
    allowed_domains = ["www.zaobao.com"]
    start_urls = ['http://www.zaobao.com/news/china']
 #   rules = (Rule(LinkExtractor(allow=('news/china/story\d+-\d+',),restrict_xpaths=()),callback='parse_item',follow=True),)
    def parse(self, response):
        print u'第二程序'
        print response.url
