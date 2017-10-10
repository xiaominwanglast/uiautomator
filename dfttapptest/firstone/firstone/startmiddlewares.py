#coding:utf-8
import logging
logger = logging.getLogger(__name__)
class ModifyStartRequest(object):
    def process_start_requests(self, start_requests, spider):
        print '-'*50
        print start_requests
        print spider.name
        print '-'*50
        logging.debug("#### 2222222 start_requests %s , spider %s ####" % (start_requests, spider))
        last_request = []
        for one_request in start_requests:
            logging.debug("#### one_request %s , spider %s ####" % (one_request, spider))
            last_request.append(one_request)
        logging.debug("#### last_request %s ####" % last_request)
        return last_request
