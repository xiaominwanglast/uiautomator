#coding:utf-8
from scrapy.http import Request
import time
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
class TopNews(CrawlSpider):
    name='topnews'
    allowed_domains=['163.com']
    start_urls=['http://news.163.com/rank/']
    now_time=time.strftime('%m%d',time.localtime(time.time()))
    rules=[Rule(LinkExtractor(allow=('^http://.*?.163.com/17/{}/\d+/.*?\.html'.format(now_time),),deny_domains=('gg.163.com','play.163.com','w.163.com','d.163.com','caozhi.news.163.com')),callback='parse_rank')]
    def parse_rank(self,response):
        if response.xpath('//div[@class="post_content_main"]/h1/text()').extract():
            title=response.xpath('//div[@class="post_content_main"]/h1/text()').extract_first().encode('gb18030')
            resource=''.join(response.xpath('//div[@class="post_content_main"]/div/text()').extract()).replace('\n','').replace(' ','')
            print resource.encode('gb18030')
        if response.xpath('//div[@class="post_text"]/p/text()').extract():
            body=''.join(response.xpath('//div[@class="post_text"]/p/text()').extract())
            print body.encode('gb18030')

