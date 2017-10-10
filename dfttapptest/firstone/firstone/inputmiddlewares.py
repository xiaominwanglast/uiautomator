#coding:utf-8
import logging
# from scrapy.shell import inspect_response
logger = logging.getLogger(__name__)
class SpiderInputMiddleware(object):
    def process_spider_input(self, response, spider):
        # inspect_response(response, spider)
        logging.debug("#### 33333 response %s , spider %s ####" % (response, spider))
        return
