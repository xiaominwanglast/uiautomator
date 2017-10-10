#coding:utf-8
import requests
import urllib2
from bs4 import BeautifulSoup
proxy='119.23.129.24:3128'
#'119.23.129.24:3128'
#110.73.33.75:8123
session=requests.Session()
'''
rq=session.get('http://tgtvs.dftoutiao.com/tg.php?channel_id=as_test_1')
print rq.headers
for i in session.cookies:
    print i.name,i.value
'''

rq=session.get('http://ip.filefab.com/index.php',proxies={'http':proxy},timeout=5)
bs=BeautifulSoup(rq.text,'lxml')
#print bs.find('h1',attrs={'id':"ipd"}).get_text()

url1='https://channel.dftoutiao.com/cookie.php?bundleid=com.gaoxin.EastNewsAppstore'
rp=session.get(url1,proxies={'http':proxy},allow_redirects=False,cookie=False)
print rp.headers


