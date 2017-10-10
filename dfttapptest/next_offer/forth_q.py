#coding:utf-8
#requests ip伪装，cookie登陆获取，利用cookie进行登陆
#ip伪装
import requests
from bs4 import BeautifulSoup
header={ 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:51.0) Gecko/20100101 Firefox/51.0'}
url='http://ip.filefab.com/index.php'
rq=requests.get(url,headers=header,proxies={'http':'202.121.178.244:8080'})
bs=BeautifulSoup(rq.text,'lxml')
print bs.find('h1',attrs={'id':"ipd"}).get_text()

#cookie登陆获取
import urllib
url='http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LRRiM'
data={'username':'weisuen',
      'password':'aA123456',
      'loginsubmit':'true',
      'formhash':'b555ca79'}
session=requests.session()
rq=session.post(url,data)
for i in session.cookies:
    print i.name,i.value

rq1=session.get('http://bbs.chinaunix.net/home.php?mod=spacecp')
print rq1.text