#coding:utf-8
import urllib2
import requests,csv
from bs4 import BeautifulSoup
import pymongo
cn=pymongo.MongoClient('127.0.0.1',27017)
db=cn.appstore
table=db.testtable
'''
class RedirctHandler(urllib2.HTTPRedirectHandler):
    """docstring for RedirctHandler"""
    def http_error_301(self, req, fp, code, msg, headers):
        pass
    def http_error_302(self, req, fp, code, msg, headers):
        pass
url='http://tgtvs.dftoutiao.com/tg.php?channel_id=as_test_1'
data1={'channel_id':'as_test_1'}
debug_handler = urllib2.HTTPHandler(debuglevel=1)
opener = urllib2.build_opener(debug_handler)
rq=urllib2.Request(url,data=urllib.urlencode(data1))
ro=opener.open(rq,timeout=3)

url1='https://channel.dftoutiao.com/cookie.php?bundleid=com.gaoxin.EastNewsAppstore'
data2={'bundleid':'com.gaoxin.EastNewsAppstore'}
#ro1=opener.open()
'''

url='http://tgtvs.dftoutiao.com/tg.php?channel_id=as_test_1'

#rq=session.get(url,allow_redirects=False)
#print rq.headers
path='E:\\0930\\IP.csv'
def IPpool():
    session=requests.Session()
    session.headers={'User-Agent':"Mozilla/5.0 (Linux; U; Android 1.1; en-gb; dream) AppleWebKit/525.10  (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2",
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Accept-Encoding': 'gzip,deflate,sdch'}
    reader=csv.reader(open(path))
    for row in reader:
        proxy=row[0]+':'+row[1]
        '''
        rq=session.get('http://ip.filefab.com/index.php',proxies={'http':proxy},timeout=5)
        bs=BeautifulSoup(rq.text,'lxml')
        print bs.find('h1',attrs={'id':"ipd"}).get_text()
        '''
        #url1='https://channel.dftoutiao.com/cookie.php?bundleid=com.gaoxin.EastNewsAppstore'
        url1='http://ip.filefab.com/index.php'
        req(session,url1,proxy)
def req(session,url_,proxy,times=2):
    try:
        rq=session.get(url_,proxies={'http':proxy},allow_redirects=False,timeout=3)
        bs=BeautifulSoup(rq.text,'lxml')
        print bs.find('h1',attrs={'id':"ipd"}).get_text()
    except Exception as e:
        print e
        if times<1:
            return None
        else:
            times-=1
            req(session,url_,proxy,times=times)
    else:
        print proxy
        table.save({'ip':proxy,})


def IPspider(numpage):
    csvfile = file(path, 'wb')
    writer = csv.writer(csvfile)
    url='http://www.xicidaili.com/nn/{}'
    headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0'}
    for num in xrange(1,numpage+1):
        ipurl=url.format(num)
        print 'Now downloading the '+str(num*100)+' ips'
        request=urllib2.Request(ipurl,headers=headers)
        content=urllib2.urlopen(request,timeout=2).read()
        bs=BeautifulSoup(content,'html.parser')
        res=bs.find_all('tr')
        for item in res:
            try:
                temp=[]
                tds=item.find_all('td')
                temp.append(tds[1].text.encode('utf-8'))
                temp.append(tds[2].text.encode('utf-8'))
                writer.writerow(temp)
            except IndexError:
                pass
IPspider(3)
IPpool()
'''
proxy='119.23.129.24:3128'
session=requests.Session()
session.cookies.clear()
session.headers={'User-Agent':"Mozilla/5.0 (Linux; U; Android 1.1; en-gb; dream) AppleWebKit/525.10  (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2",
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Accept-Encoding': 'gzip,deflate,sdch'}
rq=session.get('http://ip.filefab.com/index.php',proxies={'http':proxy},timeout=5)
bs=BeautifulSoup(rq.text,'lxml')
print bs.find('h1',attrs={'id':"ipd"}).get_text()
url1='https://channel.dftoutiao.com/cookie.php?bundleid=com.gaoxin.EastNewsAppstore'
rp=session.get(url1,proxies={'http':proxy},allow_redirects=False)
print rp.headers
'''
