#coding:utf-8
import requests
import random
import json
import time
sleeptime=[]
daily_times=0
def url_request(dic_data,times=3):
    url=dic_data['url']
    data=dic_data['data']
    try:
        rq=requests.post(url=url,data=data)
        response=rq.text
        return response
    except:
        if times==0:
            return None
        else:
            times-=times
            url_request(dic_data,times=times)
def run(accid,user):
    signmsg=signbonus=readmsg=dspmsg=pushmsg=shaimsg=''
    signurl='https://kp.dftoutiao.com/sign'
    device=['ios','Android']
    readurl='https://kp.dftoutiao.com/taskfinish/read_news'
    readdata={'url':readurl,'data':{'accid':accid}}
    dspurl='https://kp.dftoutiao.com/taskfinish/read_adv'
    dspdata={'url':dspurl,'data':{'accid':accid}}
    signdata={'url':signurl,'data':{'accid':accid,'client':random.choice(device)}}
    pushurl='https://kp.dftoutiao.com/taskfinish/read_push_news'
    pushdata={'url':pushurl,'data':{'accid':accid}}
    shaiurl='https://kp.dftoutiao.com/taskfinish/zhuangbility'
    shaidata={'url':shaiurl,'data':{'accid':accid}}

    response_shai=url_request(shaidata)
    response_shai=json.loads(response_shai)
    if not response_shai['status']:
        shaimsg=response_shai['msg']
    shaibonus='5'
    response_sign=url_request(signdata)
    if response_sign:
        response_sign=json.loads(response_sign)
        signmsg=response_sign['msg']
        if response_sign['status']:
            signbonus=response_sign['bonus']
    for i in range(15):
        response_read=url_request(readdata)
        response_read=json.loads(response_read)
        if response_read and response_read['msg']=='time max':
            readmsg=response_read['msg']
            break
    readbonus='10'
    for i in range(15):
        response_dsp=url_request(dspdata)
        response_dsp=json.loads(response_dsp)
        if response_dsp and response_dsp['msg']=='time max':
            dspmsg=response_dsp['msg']
            break
    dspbonus='10'
    for i in range(10):
        response_push=url_request(pushdata)
        response_push=json.loads(response_push)
        if response_push and response_push['msg']=='time max':
            pushmsg=response_push['msg']
    pushbonus='5'
    print user+':->'u'签到 '+signmsg+'+'+signbonus+u' 阅读文章 '+readmsg+'+'+readbonus+u' 欣赏广告 '+dspmsg+'+'+dspbonus+u' 阅读推送 '+pushmsg+'+'+pushbonus+u' 晒收入 '+shaimsg+'+'+shaibonus

def money(accid,user):
    global sleeptime
    response_sharetree_msg=''
    treeurl='https://kp.dftoutiao.com/taskfinish/harvest_tree'
    treedata={'url':treeurl,'data':{'accid':accid}}
    response_tree=url_request(treedata)
    response_tree=json.loads(response_tree)
    if response_tree["code"]=="0":
        sharetree='https://kp.dftoutiao.com/taskfinish/share_tree'
        sharetreedata={'url':sharetree,'data':{'accid':accid}}
        response_sharetree=url_request(sharetreedata)
        response_sharetree=json.loads(response_sharetree)
        response_sharetree_msg=response_sharetree['msg']


def main():
    global daily_times
    for acc in accids:
        run(acc['accid'],acc['user'])
    daily_times+=1
if __name__=='__main__':
    accids=[{'accid':'101816052','user':u'洒洒'}]
    main()
    '''
    accids=[{'accid':'100896428','user':u'01825390'},{'accid':'100725033','user':u'01924915'},{'accid':'100726655','user':u'62860620'},{'accid':'101664738','user':u'21145335'},
            {'accid':'101347656','user':u'16706869'},{'accid':'101856872','user':u'17058130'},{'accid':'101856980','user':u'21049686'},{'accid':'101857125','user':u'21603855'},
            {'accid':'100640811','user':u'陈珊'},{'accid':'101509563','user':u'高慧敏'},{'accid':'100900255','user':u'李鑫'},{'accid':'100563712','user':u'何刚'},
            {'accid':'100542322','user':u'何刚1'},{'accid':'100641121','user':u'邓琳仪'},{'accid':'100536735','user':u'程远'},{'accid':'100900247','user':u'徐培杰'},
            {'accid':'100503319','user':u'刘伟'},{'accid':'100609850','user':u'谭宝林'},{'accid':'100000093','user':u'钟锦'},{'accid':'101885536','user':u'程远1'}]

    while True:
        blocktime=time.strftime('%H:%M',time.localtime(time.time()))
        if blocktime=='06:00'and daily_times==0:
            main()
        if blocktime=='23:00'and daily_times==1:
            daily_times-=1
    '''

