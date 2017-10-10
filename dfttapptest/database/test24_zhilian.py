# coding:utf-8
import re
import requests
import urllib2
import datetime
from bs4 import BeautifulSoup
from pymongo import MongoClient
from multiprocessing import Pool

#开启数据库
cn=MongoClient('localhost',27017)
db=cn.job
table=db.zhilian
#初始化数据库
table.remove({})

#初始化测试数据
job=u'测试'
place=u'全国'
job_url=urllib2.quote(job.encode('utf-8'))
place_url=urllib2.quote(place.encode('utf-8'))

#获取页数
def get_page():
    url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl={}&kw={}&p=1&kt=3'.format(place_url,job_url)
    wbdata = requests.get(url).content
    soup = BeautifulSoup(wbdata, 'lxml')
    items = soup.select("div#newlist_list_content_table > table")
    count = len(items) - 1
    # 每页职位信息数量
    print u'每个页面的有%s条数据'%count
    job_count_data = soup.find('span',class_="search_yx_tj")
    job_count=re.search(r'\d{1,}',job_count_data.get_text()).group()

    print u'满足搜索条件职位有%s个'%job_count
    # 搜索结果页数
    pages = (int(job_count)/count) + 1
    print u'一共有%d页面'%pages
    return pages

#主程序
def get_zhaopin(page_):
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl={}&kw={}&p={}&kt=3'.format(place_url,job_url,page_)

    wbdata = requests.get(url,headers=headers).content
    soup = BeautifulSoup(wbdata,'lxml')

    job_name = soup.select("table.newlist > tr > td.zwmc > div > a")
    salarys = soup.select("table.newlist > tr > td.zwyx")
    locations = soup.select("table.newlist > tr > td.gzdd")
    times = soup.select("table.newlist > tr > td.gxsj > span")

    for name, salary, location, time in zip(job_name, salarys, locations, times):
        data = {
            'name': name.get_text(),
            'salary': salary.get_text(),
            'location': location.get_text(),
            'time': time.get_text(),
        }
        table.insert_one(data)

#开启5进程
if __name__=="__main__":
    page=get_page()
    start_time=datetime.datetime.now()
    pool = Pool(processes=5)
    pool.map_async(get_zhaopin,range(1,page+1))
    pool.close()
    pool.join()
    end_time=datetime.datetime.now()
    print u'发费总时间为：%sS'%(end_time-start_time).seconds
