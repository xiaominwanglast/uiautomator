#coding:utf-8
import requests
import re
import urllib2
from pymongo import MongoClient
from bs4 import BeautifulSoup
#抓取51job相关职位信息

def get_url():
    #连接mongo数据库
    cn=MongoClient(host='127.0.0.1',port=27017)
    db=cn.job
    table=db.autoTable

    #初始化数据
    rel=True
    line=1
    url_name=urllib2.quote(name.encode('utf-8'))
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    while rel:
        url='http://search.51job.com/list/020000,000000,0000,00,9,99,{},2,{}.html'.format(url_name.replace('%','%25'),line)
        rq=requests.get(url,headers=header)
        bs=BeautifulSoup(rq.content,'html.parser')
        page=bs.find('span',class_="td").string
        page_num=re.search('\d{1,}',page).group()
        if line<=int(page_num):
            print u'正在抓取%s页面信息'%line
        #   print bs.prettify(encoding='gbk')
            div=bs.find_all('div',class_="el")
            for data in div:
                if data.find_all('p', class_="t1 "):
                    jobdic={}
                    #正则获取需要的信息
                    jobdic['job_name']=data.p.span.a.attrs['title']
                    jobdic['job_request_href']=data.p.span.a.attrs['href']
                    jobdic['job_company']=data.find('span',class_="t2").a.attrs['title']
                    jobdic['job_place']=data.find('span',class_="t3").string
                    jobdic['job_money']=data.find('span',class_="t4").string
                    jobdic['job_pushtime']=data.find('span',class_="t5").string
                    #存储数据
                    table.save(jobdic)
            line+=1
        else:
            rel=False
if __name__=='__main__':
    name=u'自动化测试工程师'
    get_url()
