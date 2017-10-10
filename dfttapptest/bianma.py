#coding:utf-8
import redis
import requests
import random
import bs4
host='172.18.5.162'
port=6379
db=1
r=redis.Redis(host=host,port=port,db=db)
agent= ["Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",]
header={'User-Agent':random.choice(agent)}
#print r.llen('b2b_url:start_urls')
for url in r.lrange('b2b_url:start_urls',0,-1):
    rq=requests.get(url=url,headers=header)
    bs=bs4.BeautifulSoup(rq.text,'lxml')

    print rq.text.encode('gb18030')
    break