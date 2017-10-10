# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from items import JdSpiderItem
from pymongo import MongoClient
class JdSpiderPipeline(object):
    def __init__(self):
        self.cn=MongoClient('127.0.0.1',27017)
        self.db=self.cn.jd
        self.table=self.db.jd_table
    def process_item(self, item, spider):
        if isinstance(item, JdSpiderItem):
            print 'PornVideoItem True'
            try:
                self.table.insert(dict(item))
            except Exception:
                pass
        return item
