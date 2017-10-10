#coding:utf-8
import requests
import hashlib
import json
all_data=[]
def run(user,accid):
    global all_data
    url='https://kp.dftoutiao.com/sign/get_month_sign_info'
    data={'accid':accid}
    rq=requests.post(url,data=data)
    js=json.loads(rq.text)
    allbonus=0
    for i in js['data']:
        allbonus=allbonus+int(i['get_bonus'])+int(i['ex_bonus'])
    dic_={'accid':accid,'user':user,'bonus':allbonus}
    all_data.append(dic_)
if __name__=='__main__':
    accids=[{'accid':'100896428','user':u'01825390'},{'accid':'100725033','user':u'王孝敏'},{'accid':'100726655','user':u'62860620'},{'accid':'101664738','user':u'21145335'},
            {'accid':'101347656','user':u'16706869'},{'accid':'101856872','user':u'17058130'},{'accid':'101856980','user':u'21049686'},{'accid':'101857125','user':u'21603855'},
            {'accid':'100640811','user':u'陈珊'},{'accid':'101509563','user':u'高慧敏'},{'accid':'100900255','user':u'李鑫'},{'accid':'100563712','user':u'何刚'},
            {'accid':'100542322','user':u'何刚1'},{'accid':'100641121','user':u'邓琳仪'},{'accid':'100536735','user':u'程远'},{'accid':'100900247','user':u'徐培杰'},
            {'accid':'100503319','user':u'刘伟'},{'accid':'100609850','user':u'谭宝林'},{'accid':'100000093','user':u'钟锦'},{'accid':'101885536','user':u'程远1'},
            {'accid':'100238693','user':u'洒洒'},{'accid':'101902752','user':u'胡俊毅'},{'accid':'100000062','user':u'志勇'},{'accid':'100001122','user':u'新妮'}]
    for i in accids:
        run(i['user'],i['accid'])
for i in all_data:
    print i['user'],i['bonus']
'''
print '****'*20
url1='https://api.dftoutiao.com/mission/getall'
data1={'accid':'178164325','qid':'dftt170726','oem':'DFTT','version':'1.7.9','plantform':'android'}
rq1=requests.post(url1,data=data1)
print rq1.text

def psw(pwd):
    old_pws=hashlib.md5()
    old_pws.update(pwd)
    return old_pws.hexdigest()

url2='https://api.dftoutiao.com/globaluc/loginwithpwd'
data={'mobile_num':'13262860620',
      'password': psw('wang12345'),
      'imei':'',
      'qid':'dftt170726',
      'idfa':'3b1488d50807c1df',
      'softname':'DFTTAndroid',
      'softid':'DFTT',
      'softver':'1.7.8',
      'os':'Android',
      'os_version':'Android4.4.0',
      'device':'Note 2'
      }
rq=requests.post(url2,data=data)
js=json.loads(rq.text)
print js
'''
