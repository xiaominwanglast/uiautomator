#coding:utf-8
import requests
url='http://b2b.huangye88.com/guangdong/'
url1='http://b2b.huangye88.com/guangdong/it/'
url2='http://b2b.huangye88.com/qiye2382048/'
header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.6 Safari/538.36'}
session=requests.Session()
rq=session.get(url,headers=header)
print rq.status_code
rq1=session.get(url,headers=header)
print rq1.status_code
rq2=session.get(url2,headers=header)
print rq2.status_code