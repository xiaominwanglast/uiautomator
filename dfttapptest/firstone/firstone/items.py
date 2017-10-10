# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FirstoneItem(scrapy.Item):
    _id=scrapy.Field()
    news_type=scrapy.Field()
    num=scrapy.Field()
    baidu_url=scrapy.Field()
    focus_num=scrapy.Field()

#ww=FirstoneItem(_id=1,news_type='hot',num=23123,baidu_url='http://www.baidu.com',focus_num=32423)
#print ww['_id']