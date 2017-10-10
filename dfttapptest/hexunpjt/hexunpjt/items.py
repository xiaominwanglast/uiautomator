# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HexunpjtItem(scrapy.Item):
    #w文章name
    name=scrapy.Field()
    #文章链接
    url=scrapy.Field()
    #文章阅读数
    hits=scrapy.Field()
    #文章评论数
    comment=scrapy.Field()