#coding:utf-8
import urllib2,re,random
import requests
import sys,time,csv
reload(sys)
sys.setdefaultencoding('gbk')
import HTMLParser
from bs4 import BeautifulSoup
'''
proxies = {
    "http1": "http://123.55.92.61:808",
    "http2":"http://218.0.142.124:8998"
}
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
rq=requests.get(u'http://ip.cn/',headers=headers,proxies=proxies)
bs=BeautifulSoup(rq.text,'html.parser')
well=bs.find('div',class_='well')
print well.p.encode('gbk')
'''
url='http://mini.eastday.com/mobile/170627102206054.html?ttaccid=100726655&apptypeid=DFTT&fr=jiaju'
headers='Mozilla/5.0 (Linux; Android 5.1.1; vivo X7Plus Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 V1_AND_SQ_7.1.0_692_YYB_D QQ/7.1.0.3175 NetType/4G WebP/0.3.0 Pixel/1080'

proxy=urllib2.ProxyHandler({'http':'117.143.109.137:80'})
urllib2.install_opener(urllib2.build_opener(proxy))

rq=urllib2.Request(url)
rq.add_header=[('User-Agent',headers)]
ul=urllib2.urlopen(rq,timeout=10)
text=ul.read()
bs=BeautifulSoup(text,'lxml')
if bs.find('div',id="title"):
    print bs.find('div',id="title").div.h1.string


def read(text):
    try:
        return re.compile('\d{4}-\d{2}-\d{2}').search(text).group()
    except:
        return 'No_time'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
path='E:\\0930\\douban.csv'
proxies=['42.81.58.199:80','115.29.2.139:80','101.53.101.172:9999']
write=csv.writer(file(path,'wb'))
for page in range(100):
    port=random.choice(proxies)
    print port
    proxy_handler=urllib2.ProxyHandler({"http":port})
    opener=urllib2.build_opener(proxy_handler)

    opener.addheaders=[('User-Agent',headers['User-Agent'])]
    urllib2.install_opener(opener)
    url='https://movie.douban.com/tag/'
    url_name=u'周星驰'
    url_name=url_name.encode('utf-8')
    url1=urllib2.quote(url_name)
    rq=urllib2.Request(url+url1)
    try:
        txt=urllib2.urlopen(url+url1+'?start={}'.format(page*20))
    except urllib2.URLError as e:
        print e.reason,e.code
        if e.code==403:
            continue
        else:
            break
    else:
        BS=BeautifulSoup(txt.read(),'lxml')
        cl=BS.find_all('div',class_='pl2')
        for i in cl:
            try:
                temp=[]
                move_name= i.find('a').get_text().replace(' ','').strip('\n').split('/')[0].strip('\n')
                actors= i.find('p').get_text().replace(' ','')
                action_time=read(actors)
                rate= i.find('div').findAll('span')[1].get_text()
                if rate.strip()==u'(尚未上映)' or rate.strip()==u'(评价人数不足)':
                    Num='No_data'
                else:
                    Num= i.find('div').findAll('span')[2].get_text()
                temp.append(move_name)
                temp.append(action_time)
                temp.append(rate)
                temp.append(Num)
                temp.append(actors)
                write.writerow(temp)
            except Exception as e:
                print rate,type(rate)
                print i.encode('gbk')
        print (u'第%s页信息已抓取完毕······'%page)
        time.sleep(2)

