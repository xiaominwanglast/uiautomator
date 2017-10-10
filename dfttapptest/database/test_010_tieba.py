#coding:utf-8
import requests,string
from lxml import etree
#百度贴吧获取图片
#主要使用lxml的etree.HTML
path='E:\\os\\jianc'
url = 'http://tieba.baidu.com/p/2166231880'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
r = requests.get(url,headers=header)
s = etree.HTML(r.text)
text=s.xpath('//div/img/@src')
#print text
for i in text:
    if 'imgsrc.baidu.com' in i:
        name = i.split('/')[-1]
        with open(path+'\\'+name,'wb') as f:
            cont=requests.get(i,headers=header).content
            f.write(cont)
            f.close()
            print name+u'\t已下载'