#coding:utf-8
import requests
from bs4 import BeautifulSoup
def succesion(num=0):
    #上海浦东的编号71146
    url="http://tianqi.2345.com/today-71146.htm"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:51.0) Gecko/20100101 Firefox/51.0'}
    for i in range(3):
        try:
            rq=requests.get(url,headers=headers,timeout=6)
            bs=BeautifulSoup(rq.text,'lxml')
            text1=bs.find_all('div',class_="time-main")
            text2=bs.find_all('ul',class_="parameter")
            html=html1=''
            for i in text1[0].stripped_strings:
                html=html+i
            for j in text2[0].stripped_strings:
                html1=html1+j+' '
            html1=' '.join(html1.split(' ')[2:15])
            return  u'[2345网天气提醒]'+'\n'+html+u';'+html1
        except:
            num+=1
            if num==3:
                return None
if __name__ == '__main__':
    print succesion()
