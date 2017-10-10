#coding:utf-8
import cookielib
import urllib2
import urllib
import requests
url='http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LRRiM'
data={'username':'weisuen',
      'password':'aA123456',
      'loginsubmit':'true',
      'formhash':'b555ca79'}
url_data=urllib.urlencode(data)
cookie=cookielib.CookieJar()
#urllib2.ProxyHandler()
req=urllib2.Request(url,url_data)
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
urllib2.install_opener(opener)
res=urllib2.urlopen(req)
#res=opener.open(req)
for i in cookie:
    print i.name,i.value

url2='http://bbs.chinaunix.net/home.php?mod=spacecp'
rep=urllib2.urlopen(url2)
print rep.read()


print '---------------------'
session=requests.session()
rq=session.post(url,data)
for i in session.cookies:
    print i.name,i.value

cookie1=rq.cookies
for i in cookie1:
    print i.name,i.value

rq1=session.get('http://bbs.chinaunix.net/home.php?mod=spacecp')
print rq1.text

