# -*- coding: utf-8 -*-
from scrapy.spiders import CSVFeedSpider


class MycsvspiderSpider(CSVFeedSpider):
    name = 'mycsvspider'
    allowed_domains = ['iqianyue.com']
    start_urls = ['http://yum.iqianyue.com/weisuenbook/pyspd/part12/mydata.csv']
    headers = ['name', 'sex', 'addr', 'email']
    delimiter = ','

    # Do any adaptations you need here
    #def adapt_response(self, response):
    #    return response
    def parse_row(self, response, row):
        i = {}
        i['name'] = row['name']
        i['sex'] = row['sex']
        print u'名字是：'+ i['name']
        print u'性别是：'+ i['sex']
        print '--'*8
        return i
