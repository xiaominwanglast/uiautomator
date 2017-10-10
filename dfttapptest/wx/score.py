#coding:utf-8
import re,urllib2
import socket
import HTMLParser
from lxml import etree
def get(out_times=3):
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    url='http://staffbonus.dftoutiao.com/staff'
    try:
        rq=urllib2.Request(url,headers=headers)
        ul=urllib2.urlopen(rq,timeout=10)
        bs=etree.HTML(ul.read())
    except urllib2.HTTPError as e:
        print e.code
    except socket.timeout as e:
        if e.message=='timed out':
            out_times-=1
            if out_times>0:
                print u'访问超时，正式重试第%d次连接······'%out_times
                get(out_times=out_times)
            else:
                return u'三次访问超时，请尝试重新打开'
    else:
        fa=bs.xpath('//tr[@data-is-dftt="1"]')
        list_all=[]
        for i in fa:
            dict_={}
            text=etree.tostring(i)
            cont=HTMLParser.HTMLParser().unescape(text)
          #  print text
            pt=r'<td class="ok">(.*?)</td>|<td class="">(.*?)</td>'
            score=re.findall(re.compile(pt),cont)
         #   print score[0][0],score[0][1],score[1][0],score[1][1]
            if score[0][0]!='':
                dict_['name']=score[0][0].split('(')[0].strip()
                dict_['result']='pass'
                dict_['score']=score[1][0]
            else:
                dict_['name']=score[0][1].split('(')[0].strip()
                dict_['result']='fail'
                dict_['score']=score[1][1]
            list_all.append(dict_)
        return list_all
def do_data():
    listname=[u"仲　锦",u"张洒洒",u"李鑫1",u"徐培杰",u"侯新妮",u"刘　伟",u"田振华",u"周志勇",u"邓琳仪",u"谭宝林",u"高慧敏",u"程　远",u"谭佳佳",u"范石磊",u"何　刚",u"岳观文",u"王孝敏",u"许　红"]
    list_data=get()
    if type(list_data)==list:
        str_=''
        for name in listname:
            for i in list_data:
            #  print i['name']
                if i['name']==name:
                    str_=str_+'\t'+name+'\t'+i['score']+'\t'+i['result']+'\n'
                    break
        return str_
    else:
        return  list_data
if __name__=='__main__':
    print do_data()