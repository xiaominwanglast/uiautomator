#coding:utf-8
from lxml import etree
#eval可以将unicode与str类型数转化成字典数据dict
import requests
url=u'http://api.bilibili.com/archive_stat/stat?aid={}'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
i=1
while True:
    text=requests.get(url.format(i),headers=header)
    if text.status_code==200:
        cont=text.text
        print eval(cont)['data']['view'],eval(cont)['data']['danmaku'],eval(cont)['data']['reply'],eval(cont)['data']['favorite']
        if eval(cont)['data']['favorite']>10000:
            print url.format(i)+'\n'
    i+=1