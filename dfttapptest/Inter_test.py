#coding:utf-8
import json
import re
import xlrd
import time
import base64
import subprocess
import os

log_path=os.path.dirname(os.getcwd())+'\\dfttapptest\\'+'temp.txt'
untest_logpath=os.path.dirname(os.getcwd())+'\\dfttapptest\\'+'undeal_logpath.txt'
url_path=os.path.dirname(os.getcwd())+'\\dfttapptest\\'+'inter_url.xls'
data=os.path.dirname(os.getcwd())+'\\dfttapptest\\'+'data.txt'

wk=xlrd.open_workbook(url_path)
sheet=wk.sheet_by_name('Sheet1')
list_data_fi=[]
for i in range(1,sheet.nrows):
    dic_data={'id'  :sheet.cell_value(i,0),
              'name':sheet.cell_value(i,1).strip(),
              'int' :sheet.cell_value(i,2).strip(),
              'url' :sheet.cell_value(i,4).strip()}
    list_data_fi.append(dic_data)

def read_log():
    with open(log_path,'r') as f:
        text=f.read()
    new_text=text.split('----------')
    list_data=[]
    for i in new_text:
        if i!='':
            i=i.replace('\\t','|')
            try:
                if "paramjson" not in i:
                    js=json.loads(i)
                    list_data.append(js)
                elif "paramjson" in i:
                    js={}
                    parameters={}
                    paramjson={}
                    #获取url
                    js['url']=re.findall('"url":"(.*?)"',i)[0]
                    #获取position
                    if re.findall('"position":"(.*?)"',i):
                        parameters['position']=re.findall('"position":"(.*?)"',i)[0]
                    #获取param
                    if re.findall('"param":"(.*?)"',i):
                        parameters['param']=re.findall('"param":"(.*?)"',i)[0]
                    #获取paramjson内appver
                    if re.findall('"appver":"(.*?)",',i):
                        paramjson['appver']=re.findall('"appver":"(.*?)",',i)[0]
                    #获取paramjson内typeid
                    if re.findall('"typeid":"(.*?)"',i):
                        paramjson['typeid']=re.findall('"typeid":"(.*?)"',i)[0]
                    #获取paramjson内devicetype
                    if re.findall('"devicetype":"(\d)"',i):
                        paramjson['devicetype']=int(re.findall('"devicetype":"(\d{1,})"',i)[0])
                    parameters['paramjson']=paramjson
                    js['parameters']=parameters
                    #获取time
                    if re.findall('"time":"(.*?)"',i):
                        js['time']=re.findall('"time":"(.*?)"',i)[0]
                    list_data.append(js)
            except:
                try:
                    if '"info"' in i:
                        i=i.replace('\\','')
                        js={}
                        parameters={}
                        info={}
                        js['url']=re.findall('"url":"(.*?)"',i)[0]
                        #获取parameters内的ver
                        if re.findall('"ver":"(.*?)"',i):
                            parameters['ver']=re.findall('"ver":"(.*?)"',i)[0]
                        #获取info的name
                        if re.findall('"name":"(.*?)"',i):
                            info['name']=re.findall('"name":"(.*?)"',i)
                        parameters['info']=info
                        js['parameters']=parameters
                        #获取time
                        if re.findall('"time":"(.*?)"',i):
                            js['time']=re.findall('"time":"(.*?)"',i)[0]
                        list_data.append(js)
                    elif 'order.php' in i:
                        i=i.replace('\\','').replace('\t','').replace('\n','').replace(' ','').replace('"[','[').replace(']"',']')
                        js=json.loads(i)
                        list_data.append(js)
                    else:
                        file_=open(untest_logpath,'a+')
                        file_.write(i)
                        file_.close()
                except:
                    file_=open(untest_logpath,'a+')
                    file_.write(i)
                    file_.close()
    return list_data

def deal_url():
    list_url=read_log()
    for i in list_data_fi:
        for j in list_url:
            if re.findall('.*?(%s)$'%('/'+i['int']),j['url'].strip()) and list(set(i['int'].split('/')).difference(set(j['url'].strip().split('/')))) == []:
                if j['url'].strip()==i['url']:
                    print '==============================================================='
                    print j['time']
                    print u"正确域名:>>"+j['url']
                    deal_param(j)
                else:
                    print '==============================================================='
                    print j['time']
                    print u"!!!!!错误域名:>>"+j['url']
                    print u"!!!!!错误域名:>>"+j['url']
                    print u"!!!!!错误域名:>>"+j['url']
                    time.sleep(20)

def deal_param(al):
    file_=open(data,'a+')
    file_.write('-----------------------------------------'+'\n')
    file_.write(str(al)+'\n')
    file_.close()
    if 'code' in al['parameters'].keys():
        print u"code解码:>>"+'\n'+base64.b64decode(al['parameters']['code']).decode('utf-8')
        print '------------------------------------------------------------'
    elif 'info' in al['parameters'].keys():
        if 'name' in al['parameters']['info'].keys():
            print u"info信息:>>"+'\n'+(','.join(al['parameters']['info']['name'])).decode('utf-8')
            print '------------------------------------------------------------'
        else:
            print u"info信息:>>"+'\n'+str(al['parameters']['info'])
            print '------------------------------------------------------------'
    elif 'param' in al['parameters'].keys():
        print u"param:>>"+'\n'+al['parameters']['param'].replace('|','\t')
        print '------------------------------------------------------------'
    else:
        print u"parameters:>>"+'\n'+str(al['parameters'])
        print '------------------------------------------------------------'
def main():
    if os.path.exists(log_path):
        os.remove(log_path)
    os.popen('adb shell rm -rf sdcard/debug/statlog.log')
    while True:
        time.sleep(3)
        try:
            cmd_end='adb pull sdcard/debug/statlog.log %s'%log_path
            p_end = subprocess.Popen(cmd_end, stdout=subprocess.PIPE, shell=True)
            p_end.wait()
            deal_url()
        except:
            pass
        os.popen('adb shell rm -rf sdcard/debug/statlog.log')

main()