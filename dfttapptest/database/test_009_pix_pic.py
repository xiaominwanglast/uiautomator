#coding:utf-8
import requests,re
from lxml import etree
import time
import urllib2
#图片网站获取图片
#主要使用etree.HTML获取图片信息
def Download(path,start=1,end=165):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    for j in range(start,end):
        url='https://pixabay.com/zh/editors_choice/?media_type=photo&pagi='+ str(j)
        print url
        r = requests.get(url, headers=header)
        s = etree.HTML(r.text)
        r = s.xpath('//a/img/@data-lazy')
        for i in r:
            imglist = i.replace('__340', '_960_720')
            name = imglist.split('/')[-1]
            pic_resp = requests.get(i,headers = header)
            #二进制方式读取网页
            pic = pic_resp.content
            with open(path+'\\'+name,'wb') as f:
                f.write(pic)
                print (name+u'\t已下载')
if __name__ == '__main__':
    path='E:\\os\\jianb'
    Download(path,start=0,end=165)
