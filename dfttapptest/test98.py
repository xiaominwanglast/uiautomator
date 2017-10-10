#coding:utf-8
import requests
import urllib,json,urllib2
from time import ctime

url='https://oapi.dingtalk.com/robot/send?access_token=a119bc59bf0dfb723357271c62ec6b18e8938e72261db08a5065636cef7f9ce5'
data={"msgtype": "text","text": {"content": u'哈哈哈哈哈哈哈'}}
js_data=json.dumps(data)
print js_data,type(js_data)
header={'Content-Type':'application/json'}
rq=requests.post(url,data=js_data,headers=header)
print rq.text

'''
def dd():
    url='https://oapi.dingtalk.com/robot/send?access_token=a119bc59bf0dfb723357271c62ec6b18e8938e72261db08a5065636cef7f9ce5'
    con={"msgtype":"text","text":{"content":u"测试"}}
    jd=json.dumps(con)
    req=urllib2.Request(url,jd)
    req.add_header('Content-Type', 'application/json')
    response=urllib2.urlopen(req)
    print response.read(),ctime()
dd()
'''