# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
class DachuangwangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()
    hangye = scrapy.Field()
    leibie = scrapy.Field()
    jieduan = scrapy.Field()
    suozaidi = scrapy.Field()
    xiangmujieshao = scrapy.Field()
    jinji = scrapy.Field()
    baoming = scrapy.Field()
    caisai = scrapy.Field()
    canxing = scrapy.Field()
    fuzeren = scrapy.Field()
    duiyuan = scrapy.Field()