#coding:utf-8
from scrapy.spiders import Spider
from scrapy.http import Request
import re,time

class BaiduNews(Spider):
    name='baidunews'
    allowed_domains=['baidu.com']
    start_urls=['http://top.baidu.com/buzz?b=341']

    def parse(self, response):
        print response.url
        mode=response.xpath('//div[@class="hblock"]/ul/li/a/@href').extract()
        print mode
