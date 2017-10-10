#coding:utf-8
import urllib2
import urllib
import requests
from bs4 import BeautifulSoup
url='https://www.v2ex.com/signin'
#requests
session=requests.session()
rq=session.get(url)
bs=BeautifulSoup(rq.text,'lxml')
once= bs.find('input',attrs={'type':"hidden"}).attrs['value']
username= bs.find('input',attrs={'type':"text",'class':"sl"}).attrs['name']
password= bs.find('input',attrs={'type':"password"}).attrs['name']
data={username:'wangxiaomin',
      password:'wang12345',
      'once':once,
      'next':'/'}
res=session.post(url,data)
for i in res.cookies:
    print i.name,i.value

rq1=session.get('https://www.v2ex.com/settings')
print rq1.text.encode('gb18030')