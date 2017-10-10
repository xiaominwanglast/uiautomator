#codoing:utf-8
import scrapy
import redis
from .. import settings
from scrapy.linkextractors import LinkExtractor
from scrapy_redis.spiders import RedisSpider
from scrapy.http import Request
class WeisuenSpider(RedisSpider):
    name = 'weisuen1'
    allowed_domains = ['sohu.com']
    redis_key='b2b_url:start_urls'
    '''
    def __init__(self):
        super(WeisuenSpider,self).__init__()
        self.r=redis.Redis(host=settings.host,port=settings.port,db=1)
    def parse(self,response):
        dls=response.xpath('//dl[@onmouseover]')
        for dl in dls:
            if dl.xpath('.//h4/a/@href').extract():
                url=dl.xpath('.//h4/a/@href').extract_first()
            else:
                url=None
            if dl.xpath('.//h4/a/@title').extract():
                title=dl.xpath('.//h4/a/@title').extract_first()
            else:
                title=''
            if url:
                self.r.lpush(self.new_redis_key,url)
              #  yield Request(url=url,callback=self.parse_item,meta={'dont_redirect': True,'handle_httpstatus_list': [301, 302],'business_name':title})
    '''
    def parse(self,response):
       #items=B2BspiderItem()
        print response.url
        items={}
        items['business_name']=response.xapth('//div[@class="title"]/h1/text()').extract_first()
        items['business_body']=response.xpath('//li[@class="contro-num"]/text()').extract_first()
        items['business_place']=response.xpath('//div[@class="l-content"]/ul[2]/li[-1]/text()').extract_first()
        items['business_person']=response.xpath('//div[@class="l-content"]/ul/li[1]/a/text()').extract_first()
        items['business_iphone']=response.xpath('//div[@class="l-content"]/ul/li[3]/text()').extract_first()
        print items['business_body']
        print items['business_place']
        print items['business_person']
        print items['business_iphone']
        print items['business_name']
