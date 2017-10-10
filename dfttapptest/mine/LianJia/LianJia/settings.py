# -*- coding: utf-8 -*-

# Scrapy settings for LianJia project


BOT_NAME = 'LianJia'

SPIDER_MODULES = ['LianJia.spiders']
NEWSPIDER_MODULE = 'LianJia.spiders'


ROBOTSTXT_OBEY = False

DOWNLOAD_DELAY = 2

SCHEDULER = "scrapy_redis.scheduler.Scheduler"    #调度
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"  #去重
SCHEDULER_PERSIST = True       #不清理Redis队列
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"    #队列
#REDIS_HOST = '127.0.0.1'
#REDIS_PORT = 6379
REDIS_URL="redis://172.18.5.111:6379"


ITEM_PIPELINES = {
   'LianJia.pipelines.LianjiaPipeline': 300,
}

MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017
MONGODB_DBNAME = "lianjia"
MONGODB_DOCNAME = "saveinfo_5"
