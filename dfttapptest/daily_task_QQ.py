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
    global treetime
    treeurl='https://kp.dftoutiao.com/taskfinish/harvest_tree'
    treedata={'url':treeurl,'data':{'accid':accid}}
    response_tree=url_request(treedata)
    response_tree=json.loads(response_tree)
    if response_tree["code"]=="0":
        sharetree='https://kp.dftoutiao.com/taskfinish/share_tree'
        sharetreedata={'url':sharetree,'data':{'accid':accid}}
        url_request(sharetreedata)
    waite_time=int(response_tree['data']['remaining_time'])+60
    dict_person={'accid':accid,'user':user,'treetime':time.strftime('%H:%M',time.localtime(time.time()+waite_time))}
    if 'addbonus' in response_tree['data'].keys():
        print user+':->'u'摇钱树 '+response_tree['msg']+' +'+response_tree["data"]["addbonus"]+u' 摇钱树分享 '+'ok +5'+u' 下次领取时间点 '+dict_person['treetime']
    else:
        print user+':->'u'摇钱树 '+response_tree['msg']+u' 摇钱树分享 '+'share max'+u' 下次领取时间点 '+dict_person['treetime']
    treetime.append(dict_person)

def run_tree(accid,user):
    treeurl='https://kp.dftoutiao.com/taskfinish/harvest_tree'
    treedata={'url':treeurl,'data':{'accid':accid}}
    response_tree=url_request(treedata)
    response_tree=json.loads(response_tree)
    if response_tree["code"]=="0":
        sharetree='https://kp.dftoutiao.com/taskfinish/share_tree'
        sharetreedata={'url':sharetree,'data':{'accid':accid}}
        url_request(sharetreedata)
    waite_time=int(response_tree['data']['remaining_time'])+60
    dict_person={'accid':accid,'user':user,'treetime':time.strftime('%H:%M',time.localtime(time.time()+waite_time))}
    if 'addbonus' in response_tree['data'].keys():
        print user+':->'u'摇钱树 '+response_tree['msg']+' +'+response_tree["data"]["addbonus"]+u' 摇钱树分享 '+'ok +5'+u' 下次领取时间点 '+dict_person['treetime']
    else:
        print user+':->'u'摇钱树 '+response_tree['msg']+u' 摇钱树分享 '+'share max'+u' 下次领取时间点 '+dict_person['treetime']
    for person in treetime:
        if person['accid']==accid:
            index=treetime.index(person)
            del treetime[index]
    treetime.append(dict_person)
def main():
    global daily_times
    for acc in accids:
        run(acc['accid'],acc['user'])
    daily_times+=1

if __name__=='__main__':
    accids=[{'QQ': '2746647425', 'accid': '178164325'}, {'QQ': '746640598', 'accid': '178246576'}, {'QQ': '2198871858', 'accid': '178394095'},
            {'QQ': '3225267846', 'accid': '178466023'}, {'QQ': '911351527', 'accid': '178550272'}, {'QQ': '257275763', 'accid': '178612876'},
            {'QQ': '2959368858', 'accid': '178647508'}, {'QQ': '2631794290', 'accid': '178692463'}, {'QQ': '776910005', 'accid': '178756732'},
            {'QQ': '3565536772', 'accid': '178806349'}, {'QQ': '226340396', 'accid': '178856632'}, {'QQ': '3233350068', 'accid': '178884937'},
            {'QQ': '255146259', 'accid': '179330491'}, {'QQ': '3385605361', 'accid': '183568249'}, {'QQ': '1510684658', 'accid': '198707761'},
            {'QQ': '256203395', 'accid': '199221913'}, {'QQ': '1663720132', 'accid': '199630504'}, {'QQ': '2553347748', 'accid': '199764370'},
            {'QQ': '169003203', 'accid': '199996804'}, {'QQ': '718898947', 'accid': '200264536'}, {'QQ': '656145332', 'accid': '201097369'},
            {'QQ': '1727500963', 'accid': '137679184'}, {'QQ': '2274052689', 'accid': '208633492'}, {'WX': '13262860620', 'accid': '100587230'},
            {'WX': '17621145335', 'accid': '101793424'}]
    for i in accids:
        money(i['accid'],i['user'])
    while True:
        blocktime=time.strftime('%H:%M',time.localtime(time.time()))
        if blocktime=='06:00'and daily_times==0:
            main()
        if blocktime=='23:00'and daily_times==1:
            daily_times-=1
        for data in treetime:
            if blocktime==data['treetime']:
                run_tree(data['accid'],data['user'])

