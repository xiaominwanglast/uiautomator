#coding:utf-8
import requests
import random
import json
import os
import time
import smtplib
from email.mime.text import MIMEText
treetime=[]
daily_times=0
task_times=0
task_8=0
task_12=0
task_22=0
def url_request(dic_data,times=4):
    url=dic_data['url']
    data=dic_data['data']
    try:
        rq=requests.post(url=url,data=data)
        response=rq.text
        return response
    except:
        if times==0:
            jsdump=json.dumps({'msg':'Error','status':'Error','bonus':'Error','code':'Error','data':{'remaining_time':0,'addbonus':'Error'}})
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
    signbody=user+':->'u'签到 '+signmsg+'+'+signbonus+u' 阅读文章 '+readmsg+'+'+readbonus+u' 欣赏广告 '+dspmsg+'+'+dspbonus+u' 阅读推送 '+pushmsg+'+'+pushbonus+u' 晒收入 '+shaimsg+'+'+shaibonus+'\n'
    write_data('sign',signbody)
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
        treebody=user+':->'u'摇钱树 '+response_tree['msg']+' +'+response_tree["data"]["addbonus"]+u' 摇钱树分享 '+'ok +5'+u' 下次领取时间点 '+dict_person['treetime']+'\n'
        write_data('tree',treebody)
    else:
        print user+':->'u'摇钱树 '+response_tree['msg']+u' 摇钱树分享 '+'share max'+u' 下次领取时间点 '+dict_person['treetime']
        treebody=user+':->'u'摇钱树 '+response_tree['msg']+u' 摇钱树分享 '+'share max'+u' 下次领取时间点 '+dict_person['treetime']+'\n'
        write_data('tree',treebody)
    treetime.append(dict_person)

def run_tree(accid,user):
    treeurl='https://kp.dftoutiao.com/taskfinish/harvest_tree'
    treedata={'url':treeurl,'data':{'accid':accid}}
    response_tree=url_request(treedata)
    try:
        response_tree=json.loads(response_tree)
    except:
        response_tree={'msg':'Error','status':'Error','bonus':'Error','code':'Error','data':{'remaining_time':0,'addbonus':'Error'}}
    if response_tree["code"]=="0":
        sharetree='https://kp.dftoutiao.com/taskfinish/share_tree'
        sharetreedata={'url':sharetree,'data':{'accid':accid}}
        url_request(sharetreedata)
    waite_time=int(response_tree['data']['remaining_time'])+60
    dict_person={'accid':accid,'user':user,'treetime':time.strftime('%H:%M',time.localtime(time.time()+waite_time))}
    if 'addbonus' in response_tree['data'].keys():
        treebody=user+':->'u'摇钱树 '+response_tree['msg']+' +'+response_tree["data"]["addbonus"]+u' 摇钱树分享 '+'ok +5'+u' 下次领取时间点 '+dict_person['treetime']+'\n'
        write_data('tree',treebody)
    else:
        treebody=user+':->'u'摇钱树 '+response_tree['msg']+u' 摇钱树分享 '+'share max'+u' 下次领取时间点 '+dict_person['treetime']+'\n'
        write_data('tree',treebody)
    for person in treetime:
        if person['accid']==accid:
            index=treetime.index(person)
            del treetime[index]
    treetime.append(dict_person)

def write_data(name,word):
    if name=='sign':
        wfs=open(log_path,'a+')
        wfs.write(word.encode('utf-8'))
        wfs.close()
    if name=='tree':
        wfs=open(log_path1,'a+')
        wfs.write(word.encode('utf-8'))
        wfs.close()

def main():
    global daily_times
    for acc in accids:
        run(acc['accid'],acc['QQ'])
    daily_times+=1
def taskmain():
    for acc in accids:
        run(acc['accid'],acc['QQ'])
def mal(work_path):
    body=''
    if os.path.exists(work_path):
        with open(work_path,'rb') as fs:
            body=fs.read()
    if 'sign' in work_path:
        title=u'早签到积分任务'
    else:
        title=u'摇钱树积分任务'
    msg = MIMEText(body,'html', 'utf-8')
    msg["Subject"] = u"[%s]%s"%(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),title)
    msg["From"]    = "1727500963@qq.com"
    msg["To"]      = ','.join(['2274052689@qq.com'])
    try:
        s = smtplib.SMTP_SSL('smtp.qq.com',465)
        s.login("1727500963@qq.com","cxbobmaclmejjfgc")
        s.sendmail("1727500963@qq.com", msg["To"], msg.as_string())
        s.quit()
    except Exception,e:
        print "sendemail_Falied,the reson is %s"%e
    if os.path.exists(work_path):
        os.remove(work_path)
if __name__=='__main__':
    log_path='C:\\Users\\Administrator\\Desktop\\jifen\\sign.txt'
    log_path1='C:\\Users\\Administrator\\Desktop\\jifen\\tree.txt'
    accids=[{'QQ': '2746647425', 'accid': '178164325'}, {'QQ': '746640598', 'accid': '178246576'}, {'QQ': '2198871858', 'accid': '178394095'},
            {'QQ': '3225267846', 'accid': '178466023'}, {'QQ': '911351527', 'accid': '178550272'}, {'QQ': '257275763', 'accid': '178612876'},
            {'QQ': '2959368858', 'accid': '178647508'}, {'QQ': '2631794290', 'accid': '178692463'}, {'QQ': '776910005', 'accid': '178756732'},
            {'QQ': '3565536772', 'accid': '178806349'}, {'QQ': '226340396', 'accid': '178856632'}, {'QQ': '3233350068', 'accid': '178884937'},
            {'QQ': '255146259', 'accid': '179330491'}, {'QQ': '3385605361', 'accid': '183568249'}, {'QQ': '1510684658', 'accid': '198707761'},
            {'QQ': '256203395', 'accid': '199221913'}, {'QQ': '1663720132', 'accid': '199630504'}, {'QQ': '2553347748', 'accid': '199764370'},
            {'QQ': '169003203', 'accid': '199996804'}, {'QQ': '718898947', 'accid': '200264536'}, {'QQ': '656145332', 'accid': '201097369'},
            {'QQ': '1727500963', 'accid': '137679184'}, {'QQ': '2274052689', 'accid': '208633492'}, {'QQ': '13262860620', 'accid': '100587230'},
            {'QQ': '17621145335', 'accid': '101793424'},{'QQ': '1591389889', 'accid': '215146306'},{'QQ': '298682083', 'accid': '215169949'},
            {'QQ': '341540180', 'accid': '215372413'},{'QQ': '428695674', 'accid': '215388730'},{'QQ': '3177424709', 'accid': '217503946'},
            {'QQ': '3106699800', 'accid': '217520263'},{'QQ': '1639631600', 'accid': '217539244'},{'QQ': '3356146535', 'accid': '220306807'},
            {'QQ': '168795158', 'accid': '220331782'}, {'QQ': '228715448', 'accid': '220365415'}, {'QQ': '204146323', 'accid': '220374406'},
            {'QQ': '891496706', 'accid': '221038075'}, {'QQ': '1769292561', 'accid': '221060053'}, {'QQ': '169114040', 'accid': '221087026'},
            {'QQ': '715006549', 'accid': '221096017'}, {'QQ': '166539116', 'accid': '221103676'}, {'QQ': '180822319', 'accid': '221214565'},
            {'QQ': '298756101', 'accid': '221337442'}, {'QQ': '813809374', 'accid': '221347765'}, {'QQ': '1655113595', 'accid': '221511934'},
            {'QQ': '2126569540', 'accid': '221522923'}, {'QQ': '2747608670', 'accid': '221629150'}, {'QQ': '3377099079', 'accid': '221637475'},
            {'QQ': '1083279674', 'accid': '221253526'}, {'QQ': '1934850875', 'accid': '221595517'}]
    raw=raw_input('Please input y/Y run main task for daily task :')
    if raw=='Y' or raw=='y':
        taskmain()
    for i in accids:
        money(i['accid'],i['QQ'])
    while True:
        blocktime=time.strftime('%H:%M',time.localtime(time.time()))
        if blocktime=='06:00'and daily_times==0:
            main()
        if blocktime=='07:00' and task_times==0:
            mal(log_path)
            task_times+=1
        if blocktime=='08:00' and task_8==0:
            mal(log_path1)
            task_8+=1
        if blocktime=='14:00' and task_12==0:
            mal(log_path1)
            task_12+=1
        if blocktime=='22:30' and task_22==0:
            mal(log_path1)
            task_22+=1
        if blocktime=='23:00'and daily_times==1:
            daily_times-=1
        if blocktime=='23:00' and task_times==1:
            task_times-=1
        if blocktime=='23:00' and task_8==1:
            task_8-=1
        if blocktime=='23:00' and task_12==1:
            task_12-=1
        if blocktime=='23:00' and task_22==1:
            task_22-=1
        for data in treetime:
            if blocktime==data['treetime']:
                run_tree(data['accid'],data['user'])

