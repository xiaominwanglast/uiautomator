# coding:utf-8
import requests, time, webbrowser
from bs4 import BeautifulSoup
from multiprocessing import Pool
from pymongo import MongoClient
import urllib2
import json
import re
headers = {"Host": "www.zhihu.com",
                    "Referer": "https://www.zhihu.com/",
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87'}
session = requests.session()

def get_xsrfsrf():
    response = session.get("https://www.zhihu.com", headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    _xsrf = soup.find('input', attrs={"name": "_xsrf"})
    xsrf = _xsrf.get("value")
    return xsrf

def get_captcha():
    t = str(int(time.time() * 1000))
    captcha_url = 'https://www.zhihu.com/captcha.gif?r=' + t + "&type=login"
    r = session.get(captcha_url, headers=headers)
    with open('captcha.jpg', 'wb') as f:
        f.write(r.content)
    webbrowser.open('captcha.jpg')
    time.sleep(1)
    captcha = raw_input(u"验证码：")
    return captcha

def login(email, password):
    global cookie_
    login_url = 'https://www.zhihu.com/login/email'
    data = {
        'email': email,
        'password': password,
        '_xsrf': get_xsrfsrf(),
        "captcha": get_captcha(),
        'remember_me': 'true'}
    response = session.post(login_url, data=data, headers=headers)
    cookie_=response.cookies
    login_code = response.json()
    print login_code['msg']

def Tool(rep):
    rep=re.sub(r'<a.*?>','',rep)
    rep=re.sub(r'<i class="icon-external"></i>','',rep)
    rep=re.sub(r'</a>','',rep)
    rep=re.sub(r'<img.*?>','',rep)
    rep=re.sub(r'<b>','',rep)
    rep=re.sub(r'</b>','',rep)
    rep=re.sub(r' ','',rep)
    rep=re.sub(r'&gt;','',rep)
    rep=re.sub(r'&lt;','',rep)
    rep=re.sub(r'<br>','',rep)
    return rep.replace('\t','')

name=u'web性能测试'
#连接mongodb
cn=MongoClient(host='127.0.0.1',port=27017)
db=cn.job
table=db.zhihu_web
#初始化数据库数据
table.remove({})
def getdata(n):
    #utf-8转码中文数据
    url_name=urllib2.quote(name.encode('utf-8'))
    url='https://www.zhihu.com/r/search?q={}&offset={}'.format(url_name,n*10)
    print u'正在抓取第%d页面信息'%n
    rq = session.get(url,headers=headers)
    #  print rq.content
    js=json.loads(rq.content)
    for data in js['htmls']:
        dic={}
        bs=BeautifulSoup(data.replace('<em>','').replace('</em>','').replace('<p>','').replace('</p>',''),'lxml')
        #    print bs.prettify(encoding='gbk')
        title=bs.find('a',class_="js-title-link")
        dic['title']=title.string.replace(' ','').replace('\t','')
        if 'question' in title.attrs['href']:
            dic['question']='https://www.zhihu.com'+title.attrs['href']
        else:
            dic['question']=title.attrs['href']
        if bs.find('a',class_="author author-link"):
            dic['author']=bs.find('a',class_="author author-link").string
        else:
            dic['author']='unwrite'
        if bs.find('script',class_="content"):
            body=bs.find('script',class_="content").string
            dic['body']=Tool(body)
        else:
            dic['body']='Null'
        table.insert_one(dic)
if __name__=="__main__":
   # login('2274052689@qq.com', 'w123456')
    pool=Pool(processes=5)
    pool.map_async(getdata,range(0,50))
    pool.close()
    pool.join()