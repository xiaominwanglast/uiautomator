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
    fubonus=''
    fuurl='https://kp.dftoutiao.com/weekpresent/take'
    fudata={'url':fuurl,'data':{'accid':accid}}
    response_fu=url_request(fudata)
    response_fu=json.loads(response_fu)
    if 'bonus' in response_fu.keys():
        fubonus=response_fu['bonus']
    try:
        print user+':->'u'福袋 '+fubonus
    except:
        pass

def main():
    global daily_times
    for acc in accids:
        run(acc['accid'],acc['QQ'])
    daily_times+=1

if __name__=='__main__':
    #做福任务
    accids=[{'QQ': '3356146535', 'accid': '220306807'}, {'QQ': '168795158', 'accid': '220331782'}, {'QQ': '228715448', 'accid': '220365415'},
            {'QQ': '204146323', 'accid': '220374406'}, {'QQ': '891496706', 'accid': '221038075'}, {'QQ': '1769292561', 'accid': '221060053'},
            {'QQ': '169114040', 'accid': '221087026'}, {'QQ': '715006549', 'accid': '221096017'}, {'QQ': '166539116', 'accid': '221103676'},
            {'QQ': '180822319', 'accid': '221214565'}, {'QQ': '298756101', 'accid': '221337442'}, {'QQ': '813809374', 'accid': '221347765'},
            {'QQ': '1655113595', 'accid': '221511934'}, {'QQ': '2126569540', 'accid': '221522923'}, {'QQ': '2747608670', 'accid': '221629150'},
            {'QQ': '3377099079', 'accid': '221637475'}, {'QQ': '1083279674', 'accid': '221253526'}, {'QQ': '1934850875', 'accid': '221595517'}]
    main()

