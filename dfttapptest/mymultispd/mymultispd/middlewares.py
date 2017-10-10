#coding:utf-8
import random
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware
from settings import IPPOOL
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
class IPPOOLS(HttpProxyMiddleware):
    def process_request(self, request, spider):
        thisip=random.choice(IPPOOL)
        print u'当前使用的ip为：'+thisip['ip']
        request.meta["proxy"]="http://"+thisip['ip']