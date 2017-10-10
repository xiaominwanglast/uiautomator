#coding:utf-8
import scrapy
from scrapy.spiders import Spider
from scrapy.http import Request
from scrapy.conf import settings #从settings文件中导入Cookie，这里也可以室友from scrapy.conf import settings.COOKIE
class DemoSpider(scrapy.Spider):
    name = "demo"
    #allowed_domains = ["csdn.com"]
    start_urls = ["https://www.douban.com/people/163088717/"]
    cookie = {'ps': 'y', 'bid': 'VPb0WSOJ764', 'dbcl2': '"163088717:nZorm3cicLo"'} # 带着Cookie向网页发请求\
    headers = {
        'Connection': 'keep - alive',  # 保持链接状态
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.6 Safari/537.36'
    }
    def start_requests(self):
        yield Request(url=self.start_urls[0],headers=self.headers,cookies=self.cookie)# 这里带着cookie发出请求

    def parse(self, response):
        print response.url
        url='http://www.baidu.com'
        yield Request(url)
