# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
from items import ProjectOneItem
from items import ProjectTwoItem
from items import ProjectThreeItem
class ProjectOnePipeline(object):
    def __init__(self):
        clinet = MongoClient("localhost", 27017)
        self.db= clinet["topchina"]

    def process_item(self, item, spider):
        if isinstance(item, ProjectOneItem):
            tab=self.db[item['word']]
            try:
                tab.insert(dict(item))
            except Exception:
                pass
        if isinstance(item, ProjectTwoItem):
            tab=self.db[item['word']]
            try:
                tab.insert(dict(item))
            except Exception:
                pass
        if isinstance(item, ProjectThreeItem):
            tab=self.db[item['word']]
            try:
                tab.insert(dict(item))
            except Exception:
                pass
        return item