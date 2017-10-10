#coding:utf-8
import urllib2
url='http://example.webscraping.com'
rq=urllib2.Request(url,headers={'User-Agent':'BadCrawler'})
uo=urllib2.urlopen(url,timeout=10).read()
print uo