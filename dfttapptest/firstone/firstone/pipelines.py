# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
from items import FirstoneItem
import settings
class FirstonePipeline(object):
    def __init__(self):
        clinet = MongoClient(settings.MONGODB_HOST, settings.MONGODB_PORT)
        db = clinet[settings.MONGODB_DB]
        self.PhRes = db[settings.MONGODB_TABLE]

    def process_item(self, item, spider):
        if isinstance(item, FirstoneItem):
            try:
                self.PhRes.insert(dict(item))
            except Exception:
                pass
        return item
    def close_spider(self,spider):
        pass