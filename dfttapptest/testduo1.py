#coding=utf-8
import requests,json
import pymongo,re,time
from numpy import arange
#小鸣单车
def run(x,y,table):
    url='https://api.mingbikes.com/common/terminal/get_near_bike'
    headers={'Accept-Encoding': 'gzip',
         'User-Agent': 'Android/4.4.2 (HUAWEI/hwPE), com.xiaoming.bike/1.4.0',
         'Connection': 'Keep-Alive',
         'Host': 'api.mingbikes.com',
         'Device-UUID': 'ede5aa89-9a8b-4637-8b91-23359ebdab1e',
         'Channel': '1007',
         'Content-Type': 'application/x-www-form-urlencoded',
         'Content-Length': '45'}
    data={'lat':x,'lng':y}
    rq=requests.post(url=url,headers=headers,data=data,timeout=10)
    js=json.loads(rq.text)
    if js['msg']==u'成功':
        print 'Ok'
        for i in js['data']['bikes']:
            i['_id']=i['bike_sn']
            del i['bike_sn']
            table.save(i)
cn=pymongo.MongoClient('127.0.0.1',27017)
db=cn.ofo
table=db.ofotable
for i in arange(121.58,121.64,0.01):
    for j in arange(31.18,31.23,0.0085):
        run(j,i,table)
        time.sleep(2)

start_a=121.581207
start_b=31.215368
end_a=121.644878
end_b=31.23087
start_c=121.588106
start_d=31.188187
end_c=121.637979
end_d=31.178857





