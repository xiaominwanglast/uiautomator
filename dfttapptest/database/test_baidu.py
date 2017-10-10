#coding:Utf-8
import requests
from bs4 import BeautifulSoup
from scrapy.selector import Selector
url='http://news.baidu.com/ns?ct=0&pn=0&rn=50&ie=utf-8&tn=newstitle&word=%E5%9C%A8%E7%BA%BF%E6%97%85%E6%B8%B8'
rq=requests.get(url,timeout=3)
data=Selector(rq.text).xpath('//div[@class="result title"]')
print data
'''
bs=BeautifulSoup(rq.text,'lxml')
divs=bs.find_all('div',class_='result title')

for div in divs:
    title=div.find('div',class_='c-title-author').text.split('\xa0\xa0')
    url=div.find('h3',class_='c-title').a.get('href')
    print title
'''