#coding:utf-8
import requests
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

if __name__=='__main__':
    accids=[{'QQ': '2746647425', 'accid': '178164325'}, {'QQ': '746640598', 'accid': '178246576'}, {'QQ': '2198871858', 'accid': '178394095'},
            {'QQ': '3225267846', 'accid': '178466023'}, {'QQ': '911351527', 'accid': '178550272'}, {'QQ': '257275763', 'accid': '178612876'},
            {'QQ': '2959368858', 'accid': '178647508'}, {'QQ': '2631794290', 'accid': '178692463'}, {'QQ': '776910005', 'accid': '178756732'},
            {'QQ': '3565536772', 'accid': '178806349'}, {'QQ': '226340396', 'accid': '178856632'}, {'QQ': '3233350068', 'accid': '178884937'},
            {'QQ': '255146259', 'accid': '179330491'}, {'QQ': '3385605361', 'accid': '183568249'}, {'QQ': '1510684658', 'accid': '198707761'},
            {'QQ': '256203395', 'accid': '199221913'}, {'QQ': '1663720132', 'accid': '199630504'}, {'QQ': '2553347748', 'accid': '199764370'},
            {'QQ': '169003203', 'accid': '199996804'}, {'QQ': '718898947', 'accid': '200264536'}, {'QQ': '656145332', 'accid': '201097369'},
            {'QQ': '1727500963', 'accid': '137679184'}, {'QQ': '2274052689', 'accid': '208633492'}, {'QQ': '13262860620', 'accid': '100587230'},
            {'QQ': '17621145335', 'accid': '101793424'}]
    for i in accids:
        if accids.index(i)%5==0 and accids.index(i) !=0:
            time.sleep(180)
        money(i['accid'],i['QQ'])

