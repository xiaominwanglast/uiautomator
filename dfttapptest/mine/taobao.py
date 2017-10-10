# coding=utf-8
# usr/bin/eny python

import requests
import re
import datetime
import json
import urllib2
import pymongo
from pymongo import MongoClient
from multiprocessing import Pool
from matplotlib import pyplot as plt
import operator
from snownlp import SnowNLP

ss=[]
#连接数据库
cn=MongoClient('localhost',27017)
db=cn.job
table=db.Taobao
#初始化数据
#table.remove({})

#初始化数据信息
theme=u'牛奶'
theme_url= urllib2.quote(theme.encode('utf-8'))
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

def sovl_dict(contents):
    for content in contents:
        data_={}
        if 'itemId' in content:
            data_['goods_id'] = content['itemId']
        elif 'nid' in content:
            data_['goods_id'] = content['nid']
        else:
            data_['goods_id']  = u''
        if 'sellerId' in content:
            data_['shop_id'] = content['sellerId']
        elif 'user_id' in content:
            data_['shop_id'] = content['user_id']
        else:
            data_['shop_id'] = u''
        if 'item_loc' in content:
            data_['shop_loc'] = content['item_loc']
        else:
            data_['shop_loc'] = u''
        if 'nick' in content:
            data_['shop_name'] = content['nick']
        else:
            data_['shop_name'] = u''
        if 'title' in content:
            data_['goods_title'] = content['title'].replace('<span class=H>','').replace('</span>','')
        elif 'raw_title' in content:
            data_['goods_title'] = content['raw_title'].replace('<span class=H>','').replace('</span>','')
        else:
            data_['goods_title'] = u''
        if 'recommendReason' in content:
            data_['view_sales'] = int(re.search(r'\d{1,}',content['recommendReason']).group())
        elif 'view_sales' in content:
            data_['view_sales'] = int(re.search(r'\d{1,}',content['view_sales']).group())
        else:
            data_['view_sales'] = u''
        if 'salePrice' in content:
            data_['view_price'] = content['salePrice']
        elif 'view_price' in content:
            data_['view_price'] = content['view_price']
        else:
            data_['view_price'] = u''
        if 'url' in content:
            data_['comment_url'] = 'https:' +content['url']
        elif 'comment_url' in content:
            data_['comment_url'] = 'https:' +content['comment_url']
        else:
            data_['comment_url'] = u''
        table.insert(data_)
    #    return data_['goods_id'],data_['shop_id']


def first_content(first_url):
    #一级页面信息获取
    s = requests.get(first_url,headers=headers)
    contents = s.content.decode('utf-8')
    regex = 'g_page_config = (.+)'
    items = re.findall(regex, contents)
    items = items.pop().strip()
    items = items[0:-1]
    items = json.loads(items)
    items = items['mods']['itemlist']['data']['auctions']
    if items==[]:
        return
    else:
        sovl_dict(items)
       # goods_id,shop_id = sovl_dict(items)
       # self.second_content(goods_id, shop_id)   # 爬取二级页面
       # time.sleep(1)


def second_content(goods_id,shop_id):
    #爬取二级页面，介于淘宝与天猫的数据链不一样暂不写入
    second_url = 'https://tui.taobao.com/recommend?itemid={0}&sellerid={1}&_ksTS=&callback=jsonp&appid=3066'.format(goods_id,shop_id)
    s = requests.get(second_url,headers=headers)
    contents = s.content.decode('gbk')
    regex = 'jsonp(.+)'
    items = re.findall(regex, contents)
    items = items.pop()
    items = items[1:-2]
    items = json.loads(items)
    items = items['result']
    if items==[]:
        return
    else:
        sovl_dict(items)

def run(i):
    try:
        first_url = 'https://s.taobao.com/search?&q={}&bcoffset=&ntoffset&p4ppushleft=1%2C48&s={}'.format(theme_url, (i+1)*44)
        first_content(first_url)
        print u'正在爬取第%d页面'%i
    except Exception as e:
        print e
def multrun():
    start=datetime.datetime.now()
    pool=Pool(processes=5)
    pool.map_async(run,range(0,100))
    pool.close()
    pool.join()
    end=datetime.datetime.now()
    spend_time=(end-start).seconds
    print u'爬取100页面发费总时间为%sS'%spend_time

def deal_data():
    place=[]
    for i in table.find().sort([('view_sales',pymongo.DESCENDING)]).limit(500):
        place.append(i['shop_loc'].split(' ')[0])
    new_dic=dict([(i, place.count(i)) for i in place])
    print new_dic
 #   sorted_new_dic=sorted(new_dic.items(), key=operator.itemgetter(1))
    #画饼型图
    plt.figure()
    places=new_dic.keys()
    sizes=new_dic.values()
    plt.pie(sizes,explode=None,labels=places,colors=None,labeldistance=1.05,autopct='%3.1f%%',shadow=False,startangle=90,pctdistance=0.8)
    plt.axis('equal')
    plt.legend()
    plt.show()

def deal_first():
    place=[]
    for i in table.find().sort([('view_sales',pymongo.DESCENDING)]).limit(500):
        place.append(i['shop_loc'].split(' ')[0])
    new_place=list(set(place))
    num={}
    for i in new_place:
        num[i]=0
    for i in table.find():
        for j in new_place:
            if j in i['shop_loc']:
                num[j]=i['view_sales']+num[j]
    #画饼型图
    plt.figure()
    places=num.keys()
    sizes=num.values()
    plt.pie(sizes,explode=None,labels=places,colors=None,labeldistance=1.05,autopct='%3.1f%%',shadow=False,startangle=90,pctdistance=0.8)
    plt.axis('equal')
    plt.legend()
    plt.show()

def try_data():
    for i in table.find():
        if i['goods_id'] not in ss:
            ss.append(i['goods_id'])
        else:
            ida= table.find_one({"goods_id":i['goods_id']})["_id"]
            table.remove(ida) # 根据 id 删除一条记录

if __name__=="__main__":
 #   multrun()
    deal_data()
  #  deal_first()
  #  try_data()