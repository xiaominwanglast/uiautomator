# -*- coding: utf-8 -*-
from scrapy.spiders import XMLFeedSpider
class MyxmlspiderSpider(XMLFeedSpider):
    name = 'myxmlspider'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://blog.sina.com.cn/rss/1615888477.xml']
    iterator = 'iternodes' # you can change this; see the docs
    itertag = 'rss' # change it accordingly

    def parse_node(self, response, selector):
        i = {}
        i['title'] = selector.xpath("/rss/channel/item/title/text()").extract()
        i['link'] = selector.xpath("/rss/channel/item/link/text()").extract()
        i['author'] = selector.xpath("/rss/channel/item/author/text()").extract()
        for j in range(len(i['title'])):
            print u'第%d篇文章：'%(j+1)
            print u'标题是：'
            print i['title'][j]
            print u'链接是：'
            print i['link'][j]
            print u'作者是：'
            print i['author'][j]
            print '--'*10
        return i
