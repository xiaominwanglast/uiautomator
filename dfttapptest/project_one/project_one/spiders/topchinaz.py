#coding:utf-8
from scrapy.http import Request
from ..items import ProjectOneItem
from ..items import ProjectTwoItem
from ..items import ProjectThreeItem
from scrapy.spiders import Spider
import re
class Topchinazspider(Spider):
    name='topchinaz'
    allowed_domains=['top.chinaz.com']
    Test_url='http://top.chinaz.com/'
    Search_url='http://search.top.chinaz.com/top.aspx?'
    Global_url='http://alexa.chinaz.com/Global/'
    start_urls=['http://top.chinaz.com/hangye/','http://top.chinaz.com/diqu/','http://top.chinaz.com/alltop/']

    def parse(self, response):
        base_url=response.xpath('//li[@class="SubItem-wp"]/a/@href').extract()
        base_url.append('http://top.chinaz.com/hangye/index.html')
        base_url.append('http://top.chinaz.com/alltop/index.html')
        for url in base_url:
            if '/alltop/index' in url:
                yield Request(url=url,callback=self.parse_athref)
            elif '/hangye/' in url:
                yield Request(url=url,callback=self.parse_hdhref)
            elif '/diqu/' in url:
                yield Request(url=url,callback=self.parse_hdhref)
            elif '/Global/' in url:
                yield Request(url=url,callback=self.paser_glhref)
            else:
                pass

    def parse_hdhref(self,response):
        total_page=int(response.xpath('//div[@class="ListPageWrap"]/a/text()').extract()[-2])
        for page in range(1,total_page+1):
            if page==1:
                yield Request(url=response.url,meta={'word':response.url},callback=self.parse_page)
            else:
                yield Request(url=response.url.replace('.html','')+'_'+str(page)+'.html',meta={'word':response.url},callback=self.parse_page)

    def parse_athref(self,response):
        total_page=int(response.xpath('//div[@class="ListPageWrap"]/a/text()').extract()[-2])
        for page in range(1,total_page+1):
            if page==1:
                yield Request(url=response.url,meta={'word':response.url},callback=self.parse_index)
            else:
                yield Request(url=self.Search_url+'p='+str(page)+'&t=all',meta={'word':response.url},callback=self.parse_index)

    def paser_glhref(self,response):
        total_page=int(response.xpath('//div[@class="basePage per32"]/a/text()').extract()[-3])
        for page in range(1,total_page):
            if page==1:
                yield Request(url=response.url,callback=self.parse_global)
            else:
                yield Request(url=self.Global_url+'index_'+str(page)+'.html',callback=self.parse_global)
    def parse_page(self,response):
        href=response.xpath('//h3[@class="rightTxtHead"]/a/@href').extract()
        title=response.xpath('//h3[@class="rightTxtHead"]/a/@title').extract()
        main_url=response.xpath('//h3[@class="rightTxtHead"]/span/text()').extract()
        strong=response.xpath('//div[@class="RtCRateCent"]/strong/text()').extract()
        score=response.xpath('//div[@class="RtCRateCent"]/span/text()').extract()
        for url in href:
            yield Request(url=self.Test_url+url,callback=self.parse_item,meta={'strong':strong[href.index(url)],
                                                                                'score':re.search('\d+',score[href.index(url)]).group(),
                                                                                'mainurl':main_url[href.index(url)],
                                                                                'title':title[href.index(url)],
                                                                                'word':response.meta['word'].split('/')[-1].replace('.html','')})
    def parse_global(self,response):
        modes=response.xpath('//li[@class="clearfix"]')
        for mode in modes:
            item=ProjectThreeItem()
            _id=mode.xpath('.//div[@class="count"]/text()').extract()
            name=mode.xpath('.//div[@class="righttxt"]/h3/a[1]/text()').extract()
            mainurl=mode.xpath('.//div[@class="righttxt"]/h3/a[2]/@href').extract()
            des=mode.xpath('.//div[@class="righttxt"]/p/text()').extract()
            item['word']='global_index'
            if _id:
                item['_id']=_id[0]
            if name:
                item['name']=name[0]
            if mainurl:
                item['mainurl']=mainurl[0]
            if des:
                item['des']=des[0]
            yield item

    def parse_index(self,response):
        #单独的排行index
        modes=response.xpath('//div[@class="ContTit ulli clearfix"]')
        for mode in modes:
            item=ProjectTwoItem()
            _id=mode.xpath('.//div[@class="w90 col-red03 fz16"]/text()').extract()
            name=mode.xpath('.//div[@class="w320 PCop"]/a/text()').extract()
            weight=mode.xpath('.//div[@class="w90"]/div/img/@src').extract()
            Alexa=mode.xpath('.//div[@class="ContTit ulli clearfix"]/div[4]/text()').extract()
            PR=mode.xpath('.//div[@class="w110"]/div/img/@src').extract()
            score=mode.xpath('.//div[@class="ContTit ulli clearfix"]/div[6]/text()').extract()
            change=mode.xpath('.//div[@class="w120 col-green"]/span/text()').extract()
            item['word']='alltop_index'
            if _id:
                item['_id']=_id[0]
            if name:
                item['name']=name[0]
            if weight:
                item['weight']=re.search('\d+',weight[0]).group()
            if Alexa:
                item['Alexa']=Alexa[0]
            if PR:
                item['PR']=re.search('\d+',PR[0]).group()
            if score:
                item['score']=score[0]
            if change:
                item['change']=change[0]
            yield item

    def parse_item(self,response):
        item=ProjectOneItem()
        if response.meta['word']=='index':
            item['word']='hangye_index'
        else:
            item['word']=response.meta['word'].replace('index_','')
        item['_id']=response.meta['strong']
        item['mainurl']=response.meta['mainurl']
        item['score']=response.meta['score']
        item['name']=response.meta['title']
        item['des']=response.xpath('//p[@class="webIntro"]/text()').extract_first()
        item['company']=response.xpath('//li[@class="TMain06List-Left fl"]/p[2]/text()').extract_first()
        item['ip']=response.xpath('//li[@class="TMain06List-Cent fl"]/p[2]/text()').extract_first()
        item['domain']=response.xpath('//li[@class="TMain06List-right fl"]/p[2]/text()').extract_first()
        yield item

    def close(self, reason):
        print u'已完成'