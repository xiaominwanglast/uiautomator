#coding:utf-8
#urllib2 ip伪装，cookie登陆获取，利用cookie进行登陆
#urllib2 ip伪装
import urllib2,socket
from bs4 import BeautifulSoup
proxy=urllib2.ProxyHandler({'http':'202.121.178.244:8080'})
opener=urllib2.build_opener(proxy)
urllib2.install_opener(opener)
header={ 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:51.0) Gecko/20100101 Firefox/51.0'}
url='http://ip.filefab.com/index.php'
rq=urllib2.Request(url)
rq.add_header=[('User-Agent',header['User-Agent'])]
try:
    rq=urllib2.urlopen(rq,timeout=5)
except urllib2.URLError as e:
    if hasattr(e,'reason'):
        print e.reason
    if hasattr(e,'code'):
        print e.code
except socket.timeout:
    print socket.timeout.errno
else:
    text=rq.read()
    bs=BeautifulSoup(text,'lxml')
    print bs.find('h1',attrs={'id':"ipd"}).get_text()
#cookie获取
import urllib2
import cookielib
cookie=cookielib.CookieJar()
#cookie=cookielib.MozillaCookieJar('file.txt')获取的cookie存储到file.txt位置
#cookie.save(ignore_discard=True,ignore_expires=True)  #保存cookie到本地
bundle=urllib2.HTTPCookieProcessor(cookie)
opener=urllib2.build_opener(bundle)
urllib2.install_opener(opener)
rq=urllib2.urlopen(url)
for data in cookie:
    print data.name,data.value
#利用全局的urllib2进行其他页面访问
#加载本地cookie进行登陆
#cookie=cookielib.MozillaCookieJar()
#cookie.load('cookie.txt',ignore_discard=True,ignore_expires=True)
#利用cookie登陆
import cookielib
import urllib2
import urllib
url='http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LRRiM'
data={'username':'weisuen',
      'password':'aA123456',
      'loginsubmit':'true',
      'formhash':'b555ca79'}
url_data=urllib.urlencode(data)
cookie=cookielib.CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
urllib2.install_opener(opener)
req=urllib2.Request(url,url_data)
res=urllib2.urlopen(req)
#res=opener.open(req)
for i in cookie:
    print i.name,i.value
url2='http://bbs.chinaunix.net/home.php?mod=spacecp'
rep=urllib2.urlopen(url2)
print rep.read()

#urllib.urlretrieve(url,filename=)