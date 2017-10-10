# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ProjectOneItem(scrapy.Item):
    _id=scrapy.Field()
    mainurl=scrapy.Field()
    score=scrapy.Field()
    name=scrapy.Field()
    des=scrapy.Field()
    company=scrapy.Field()
    ip=scrapy.Field()
    domain=scrapy.Field()
    word=scrapy.Field()

class ProjectTwoItem(scrapy.Item):
    word=scrapy.Field()
    _id=scrapy.Field()
    name=scrapy.Field()
    weight=scrapy.Field()
    Alexa=scrapy.Field()
    PR=scrapy.Field()
    score=scrapy.Field()
    change=scrapy.Field()

class ProjectThreeItem(scrapy.Item):
    pass