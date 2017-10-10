#coding:utf-8
import scrapy
from ..items import DachuangwangItem
from scrapy_redis.spiders import RedisCrawlSpider

class DachuangSpiderSpider(RedisCrawlSpider):
     
    name = "dachuang"
    redis_key = 'myspider:start_urls'

#     allowed_domains = ["cy.ncss.org.cn"]
#     start_urls = []

# http://cy.ncss.org.cn/search.html?isAjax=true&ecCode=CYDS_2TH&p=page&ec_p=

    def parse(self, response):
        for page in range(1,4233):
            url = response.url + str(page)
            yield scrapy.Request(url=url,callback=self.parse_url)

    def parse_url(self, response):
        for eveXiang in response.xpath('//li'):
            url = 'http://cy.ncss.org.cn' + eveXiang.xpath("div[1]/p/a/@href").extract()[0]
            yield scrapy.Request(url=url,callback=self.parse_content)

    def parse_content(self, response):
        item = DachuangwangItem()
        item['name'] = response.xpath('//h3[@class="the-obj-name"]/text()').extract()
        item['url'] = response.url
        item['hangye'] = response.xpath('//div[@class="obj-bs-lst"]/ul/li[1]/span[2]/text()').extract()[0].replace(' ','').replace('\t','').replace('\r\n',' ')
        item['leibie'] = response.xpath('//div[@class="obj-bs-lst"]/ul/li[2]/span[2]/text()').extract()
        item['jieduan'] = response.xpath('//div[@class="obj-bs-lst"]/ul/li[3]/span[2]/text()').extract()[0].replace(' ','').replace('\n','').replace('\t','').replace('\r','')
        item['suozaidi'] = response.xpath('//div[@class="obj-bs-lst"]/ul/li[4]/span[2]/text()').extract()
        item['xiangmujieshao'] = response.xpath('//div[@class="obj-bs-intro"]/text()').extract()[0].replace(' ','').replace('\n','').replace('\t','').replace('\r','')
        item['jinji'] = response.xpath('//div[@class="obj-side-r"]/div/table/tr[1]/td/text()').extract()[0].replace(' ','').replace('\n','').replace('\t','').replace('\r','')
        item['baoming'] = response.xpath('//div[@class="obj-side-r"]/div/table/tr[2]/td/text()').extract()
        item['caisai'] = response.xpath('//div[@class="obj-side-r"]/div/table/tr[3]/td/text()').extract()
        item['canxing'] = response.xpath('//div[@class="obj-side-r"]/div/table/tr[4]/td/text()').extract()
        fzrxm = response.xpath('//div[@class="the-obj-father"]/div/table/tr[1]/th/text()').extract()[0]
        fzrgx = response.xpath('//div[@class="the-obj-father"]/div/table/tr[2]/td/text()').extract()[0]
        fzrxl = response.xpath('//div[@class="the-obj-father"]/div/table/tr[3]/td/text()').extract()[0]
        fzrsj = response.xpath('//div[@class="the-obj-father"]/div/table/tr[4]/td/text()').extract()[0]
        fzrzy = response.xpath('//div[@class="the-obj-father"]/div/table/tr[5]/td/text()').extract()[0]
        item['fuzeren'] = {u"负责人姓名":fzrxm,u"高校":fzrgx,u"学历":fzrxl,u"在校时间":fzrsj,u"专业":fzrzy,}
        duiyuan = []
        for eavDuiYuan in response.xpath('//*[@id="m_info"]/table/tr'):
            dyxm = eavDuiYuan.xpath('th/text()').extract()
            dyzz = eavDuiYuan.xpath('td[1]/text()').extract()
            dyxx = eavDuiYuan.xpath('td[2]/text()').extract()
            dyzy = eavDuiYuan.xpath('td[3]/text()').extract()
            dyxl = eavDuiYuan.xpath('td[4]/text()').extract()
            dysj = eavDuiYuan.xpath('td[5]/text()').extract()[0].replace(' ','').replace('\n','').replace('\t','').replace('\r','')
            dy = {u"队员姓名：":dyxm,u"分工：":dyzz,u"学校：":dyxx,u"专业：":dyzy,u"学历：":dyxl,u"时间：":dysj,}
            duiyuan.append(dy)
        item['duiyuan'] = duiyuan
        yield item
