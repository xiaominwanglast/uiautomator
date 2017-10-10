#coding:utf-8
import requests
import urllib2
from bs4 import BeautifulSoup
url='http://ip.filefab.com/index.php'
import socket
header={ 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:51.0) Gecko/20100101 Firefox/51.0'}

proxy=urllib2.ProxyHandler({'http':'91.98.123.183:80'})
opener=urllib2.build_opener(proxy)
urllib2.install_opener(opener)

rq=urllib2.Request(url)
rq.add_header=[('User-Agent',header['User-Agent'])]
try:
    rq=urllib2.urlopen(rq,timeout=5)
except urllib2.URLError as e:
    if hasattr(e,'reason'):
        print e.reason
    if hasattr(e,'code'):
        print e.code
except socket.error:
    print socket
else:
    text=rq.read()
    bs=BeautifulSoup(text,'lxml')
    print bs.find('h1',attrs={'id':"ipd"}).get_text()
