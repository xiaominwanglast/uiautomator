#coding:utf-8
import requests,urllib2
from  bs4 import BeautifulSoup
headers={'User-Agent':'wswp'}
url='http://example.webscraping.com/view/{}'

#rq=requests.get(url,headers=headers)
#print rq.text
i=1
while True:
    rq=urllib2.Request(url.format(i),headers=headers)
    try:
        html=urllib2.urlopen(rq,timeout=20)
    except urllib2.URLError,e:
        print e.reason
        break
    else:
        if html.code==200:
            bs=BeautifulSoup(html.read(),'lxml')
            ft=bs.find_all('td',class_='w2p_fw')
            print ft
            print ft[1].text+'\t'+ft[2].text+'\t'+ft[4].text
            i+=1
        else:
            print 'GG'