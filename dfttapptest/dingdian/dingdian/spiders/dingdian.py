#coding:utf-8
import re
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from ..items import DingdianItem

class Myspider(scrapy.Spider):
    name='dingdian'
    allowed_domains=['23us.so']
    base_url='http://www.23us.so/list/'

    def start_requests(self):
        for i in range(1,9):
            url=self.base_url+str(i)+'_1.html'
            yield Request(url,callback=self.parse)

    def parse(self, response):
        max_num=BeautifulSoup(response.text,'lxml').find('a',class_='last').string
        bashurl=str(response.url)[:-7]
        for num in range(1,int(max_num)+1):
            url=bashurl+'_'+str(num)+'.html'
            yield Request(url,callback=self.get_name)

    def get_name(self,response):
        tds=BeautifulSoup(response.text,'lxml').find_all('tr',bgcolor='#FFFFFF')
        for td in tds:
            novelname=td.find('a').get_text()
            novelurl=td.find('a')['href']
            yield Request(novelurl,callback=self.get_chapterurl,meta={'name':novelname,'url':novelurl})

    def get_chapterurl(self,response):
        item=DingdianItem()
        item['_id']=response.meta['name']
        item['novelurl']=response.meta['url']
        category=BeautifulSoup(response.text,'lxml').find('table',bgcolor='#E4E4E4').find('a').get_text()
        author=BeautifulSoup(response.text,'lxml').find('table',bgcolor='#E4E4E4').find_all('td')[1].get_text()
      #  bash_url=BeautifulSoup(response.text,'lxml').find('p',class_='btnlinks').find('a',class_='read')['href']
        name_id=int(re.findall('\d+',response.url)[1])
        item['category']=category
        item['author']=author
        item['name_id']=name_id
        yield item
