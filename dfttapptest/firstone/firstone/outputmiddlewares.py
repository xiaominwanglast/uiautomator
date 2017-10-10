#coding:utf-8
import logging
logger = logging.getLogger(__name__)
class SpiderOutputMiddleware(object):
    def process_spider_output(self, response, result, spider):
        logging.debug("#### 44444 response %s , result %s , spider %s ####" % (response, result, spider))
        return result
