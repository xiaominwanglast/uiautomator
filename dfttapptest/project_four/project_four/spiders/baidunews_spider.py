#!/usr/bin/env python
# -*- coding:utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import logging
import urllib2
from scrapy.http import Request
#logger = logging.getLogger("WshangSpider")
import datetime
class BaiduNewsSpider(scrapy.Spider):
    domain = "http://news.baidu.com/"
    name = "baidunews1"
    url_demo = "http://news.baidu.com/ns?ct=0&pn=%s&rn=50&ie=utf-8&tn=newstitle&word=%s" # 参数pn表示跳过前面多少条新闻   word表示关键词

    def start_requests(self):
        url = self.url_demo %(0,urllib2.quote(u'在线旅游'.encode('utf-8')))
        print url
        yield Request(url, callback=self.parse1, meta= {'keyword': u'在线旅游'})

    def parse1(self, response):
        keyword = response.meta.get("keyword", None)
        soup = BeautifulSoup(response.body,"lxml")
        for t in soup.find_all("div",class_="result title"):
          #  item = NewsItem()
            item={}
            url = t.find("a").get("href")       #新闻url
            title = t.find("a").text            #新闻标题
            temp_list = t.find("div",attrs={"class":"c-title-author"}).text.split(u"\xa0\xa0")
            website_name = temp_list[0]         #新闻网站名称、
            news_time = temp_list[1]
            #TODO: Some error
            now = datetime.datetime.now()
            if u"分钟前" in news_time:
                print news_time[:-3]
                struct_date = now - datetime.timedelta(minutes=int(news_time[:-3]))
                news_date = struct_date.strftime("%Y-%m-%d %H:%M:%S")
            elif u"小时前" in news_time:
                print news_time[:-3]
                struct_date = now - datetime.timedelta(hours=int(news_time[:-3]))
                news_date = struct_date.strftime("%Y-%m-%d %H:%M:%S")
            else:
                news_date = "%s-%s-%s %s:00" % (news_time[:4],news_time[5:7],news_time[8:10],news_time[12:])
            item['news_url'] = url
            item['title'] = title
            item['news_date'] = news_date
            item['referer_web'] = website_name
            item["crawl_date"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            item["keywords"] = [keyword]
           # item = SPIDER_MODULES.__class__.judge_news_crawl(item)
            if item:
                print item
            #    yield item


