#coding:utf-8
import requests,re
import HTMLParser
from lxml import etree
def douban(total=0):
    url='https://movie.douban.com/cinema/nowplaying/shanghai/'
    headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:51.0) Gecko/20100101 Firefox/51.0'}

    for i in range(3):
        try:
            rq=requests.get(url,headers=headers,timeout=5)
        except:
            total+=1
            if total==3:
                return None
            else:
                douban(total=total)
        else:
            et=etree.HTML(rq.text)
            etxp=et.xpath('//div[@id="nowplaying"]//ul[@class="lists"]/li[@class="list-item"]')
            data_all=[]
            num=[]
            for i in etxp:
                dic={}
                html=HTMLParser.HTMLParser().unescape(etree.tostring(i))
                dic['movie_name']=re.findall(r'data-title="(.*?)" data-score',html)[0]
                dic['data_actors']=re.findall(r'data-actors="(.*?)"',html)[0]
                dic['data_region']=re.findall(r'data-region="(.*?)"',html)[0]
                dic['data_score']=re.findall(r'data-score="(.*?)"',html)[0]
                data_all.append({dic['data_score']:[dic['movie_name'],dic['data_actors'],dic['data_region']]})
            for data in data_all:
                num.append(float(data.keys()[0].encode('utf-8')))
            num.sort()
            new_html=''
            for j in range(10):
                for l in data_all:
                    if num[len(num)-1-j]==float(l.keys()[0].encode('utf-8')):
                        new_html=new_html+'['+l.values()[0][0]+'] '+l.values()[0][2]+ u' 评分:'+l.keys()[0]+u' 主演:'+l.values()[0][1].replace(' ','') + '\n'
                        del data_all[data_all.index(l)]
            if new_html=='':
                return None
            else:
                return u'[豆瓣热播电影排行前10位]'+'\n'+new_html

if __name__=='__main__':
    print douban()