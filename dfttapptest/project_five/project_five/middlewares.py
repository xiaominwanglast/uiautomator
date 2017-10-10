# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random

class ProxypiderMiddleware(object):
    proxyList=['117.143.109.159:80']
    def process_request(self, request, spider):
        pro_adr = random.choice(self.proxyList)
   #     print "USE PROXY -> "+pro_adr
    #    request.meta['proxy'] = "http://"+ pro_adr

    def process_response(self, request, response, spider):
      #  print response
        return response

    def process_exception(self, request, exception, spider):
        print exception
