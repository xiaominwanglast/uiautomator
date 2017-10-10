# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.conf import settings
from pymongo import MongoClient
from items import DingdianItem
class DingdianPipeline(object):
    def __init__(self):
        clinet = MongoClient("localhost", 27017)
        db = clinet["dingdian"]
        self.PhRes = db["novel"]

    def process_item(self, item, spider):
        print 'MongoDBItem',item
        """ 判断类型 存入MongoDB """
        if isinstance(item, DingdianItem):
            print 'DingdianItem True'
            try:
                self.PhRes.insert(dict(item))
            except Exception:
                pass
        return item
