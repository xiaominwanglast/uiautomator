#coding:utf-8
from pymongo import MongoClient
import requests,re
from multiprocessing import Pool
from bs4 import BeautifulSoup
import pymongo
from matplotlib import pyplot as plt
#开启数据库
cn=MongoClient('localhost',27017)
db=cn.job
table=db.dzdp801
#初始化数据库
table.remove({})

def geturl(i):
    print u"正在抓取第%d页"%i
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    url='http://www.dianping.com/search/category/1/10/r801p{}'.format(i)
    rq=requests.get(url,headers=headers)
    bs=BeautifulSoup(rq.content,'lxml')
    div=bs.find_all('div',class_='txt')
    for mode in div:
        quyu=''
        dic_md={}
        dic_md['_id']=mode.find('div',class_='tit').a['title']
        dic_md['level']=mode.find('div',class_='comment').span['title']
        try:
            dic_md['dingping']=mode.find('a',class_='review-num').b.string
        except:
            pass
        try:
            dic_md['comment_url']='http://www.dianping.com/'+mode.find('a',class_='review-num')['href']
        except:
            pass
        if mode.find('a',class_='mean-price').b:
            dic_md['money']=mode.find('a',class_='mean-price').b.string
        if mode.find('span',class_='tag'):
            dic_md['type_']=mode.find('span',class_='tag').string
        if mode.find(attrs={'data-midas-extends':"module=5_ad_kwregion"}):
            quyu=mode.find(attrs={'data-midas-extends':"module=5_ad_kwregion"}).string
        dic_md['place']=quyu+' '+mode.find('span',class_='addr').string
        pingfen=mode.find('span',class_='comment-list')
        try:
            if re.findall('\d{1,}\.\d',pingfen.get_text()):
                list_data=re.findall('\d{1,}\.\d',pingfen.get_text())
                dic_md['kouwei']=list_data[0]
                dic_md['huanjing']=list_data[1]
                dic_md['fuwu']=list_data[2]
        except:
            pass
        table.save(dic_md)
def deal_data():
    type_=[]
    for i in table.find():
        type_.append(i['type_'])
    new_dic=dict([(i, type_.count(i)) for i in type_])
 #   sorted_new_dic=sorted(new_dic.items(), key=operator.itemgetter(1))
    #画饼型图
    plt.figure()
    places=new_dic.keys()
    sizes=new_dic.values()
    plt.pie(sizes,explode=None,labels=places,colors=None,labeldistance=1.05,autopct='%3.1f%%',shadow=False,startangle=90,pctdistance=0.8)
    plt.axis('equal')
    plt.legend()
    plt.show()

def fuwu():
    type_=[]
    n1=n2=n3=n4=n5=n6=n7=n8=n9=n10=0
    s1=s2=s3=s4=s5=s6=s7=s8=s9=s10=0
    for i in table.find():
        type_.append(i['type_'])
    for i in table.find({'fuwu':{'$exists':True}}):
        if int(i['dingping'])>100:
            if i['type_']==u'小吃快餐':
                n1+=1
                s1=s1+float(i['fuwu'])
            if i['type_']==u'面包甜点':
                n2+=1
                s2=s2+float(i['fuwu'])
            if i['type_']==u'西餐':
                n3+=1
                s3=s3+float(i['fuwu'])
            if i['type_']==u'川菜':
                n4+=1
                s4=s4+float(i['fuwu'])
            if i['type_']==u'本帮江浙菜':
                n5+=1
                s5=s5+float(i['fuwu'])
            if i['type_']==u'咖啡厅':
                n6+=1
                s6=s6+float(i['fuwu'])
            if i['type_']==u'日本菜':
                n7+=1
                s7=s7+float(i['fuwu'])
            if i['type_']==u'火锅':
                n8+=1
                s8=s8+float(i['fuwu'])
    list_type=[u'小吃快餐',u'面包甜点',u'西餐',u'川菜',u'本帮江浙菜',u'咖啡厅',u'日本菜',u'火锅']
    print n1,n2,n3,n4,n5,n6,n7,n8
    data_type=[round(s1/n1,2),round(s2/n2,2),round(s3/n3,2),round(s4/n4,2),round(s5/n5,2),round(s6/n6,2),round(s7/n7,2),round(s8/n8,2)]
    plt.xlabel(u"餐厅类型")
    plt.ylabel(u"评分")
    plt.bar(range(len(data_type)), data_type, tick_label=list_type)
    plt.show()


if __name__=="__main__":
  #  fuwu()
    pool=Pool(processes=5)
    pool.map_async(geturl,range(1,51))
    pool.close()
    pool.join()
    deal_data()



