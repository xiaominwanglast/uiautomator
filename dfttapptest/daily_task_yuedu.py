#coding:utf-8
import requests
import random
import json
import time
treetime=[]
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
            jsdump=json.dumps({'msg':'Error','status':'Error','bonus':'Error'})
            return jsdump
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
    #反馈
    fankuiurl='https://kp.dftoutiao.com/taskfinish/first_feedback'
    fakuidata={'url':fankuiurl,'data':{'accid':accid}}
    response_fankui=url_request(fakuidata)

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

def main():
    global daily_times
    for acc in accids:
        run(acc['accid'],acc['QQ'])
    daily_times+=1

if __name__=='__main__':
    #做每日任务与反馈积分
    accids=[{'QQ': '3356146535', 'accid': '220306807'}, {'QQ': '168795158', 'accid': '220331782'}, {'QQ': '228715448', 'accid': '220365415'},
            {'QQ': '204146323', 'accid': '220374406'}, {'QQ': '891496706', 'accid': '221038075'}, {'QQ': '1769292561', 'accid': '221060053'},
            {'QQ': '169114040', 'accid': '221087026'}, {'QQ': '715006549', 'accid': '221096017'}, {'QQ': '166539116', 'accid': '221103676'},
            {'QQ': '180822319', 'accid': '221214565'}, {'QQ': '298756101', 'accid': '221337442'}, {'QQ': '813809374', 'accid': '221347765'},
            {'QQ': '1655113595', 'accid': '221511934'}, {'QQ': '2126569540', 'accid': '221522923'}, {'QQ': '2747608670', 'accid': '221629150'},
            {'QQ': '3377099079', 'accid': '221637475'}, {'QQ': '1083279674', 'accid': '221253526'}, {'QQ': '1934850875', 'accid': '221595517'}]
    main()
