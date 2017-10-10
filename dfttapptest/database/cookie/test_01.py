#coding:utf-8
import urllib2
import cookielib
import sys,requests,re,random
#reload(sys)
#sys.setdefaultencoding('gbk')
file='cookie.txt'
#声明一个CookieJar对象实例来保存cookie
#cookie = cookielib.CookieJar()
cookie=cookielib.MozillaCookieJar(file)
#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler=urllib2.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener = urllib2.build_opener(handler)
#此处的open方法同urllib2的urlopen方法，也可以传入request
response = opener.open('http://www.baidu.com')
#cookie.save(ignore_discard=True,ignore_expires=True)

cookie=cookielib.MozillaCookieJar()
cookie.load(file,ignore_expires=True,ignore_discard=True)
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
rq=urllib2.Request('http://www.baidu.com')
res=opener.open(rq)
print res.read()
'''
proxies=['101.53.101.172:9999','183.78.183.156:82','42.81.58.199:80','115.29.2.139:80','124.88.67.24:80']
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
for i in range(10):
    proxie=random.choice(proxies)
    print proxie
    try:
        rq=requests.get(u'http://www.whatismyip.com.tw/',headers=headers,proxies={"http": proxie})
    except requests.ConnectionError as e:
        print e
    else:
        try:
            print re.compile(r'<h2>(.*?)</h2>').search(rq.text).group()
        except:
            print rq.text
'''