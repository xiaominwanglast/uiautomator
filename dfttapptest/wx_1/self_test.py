#coding:utf-8
import os,random,time

path= os.path.dirname(os.getcwd())+'\\wx_1\\data\\'+u'东方头条_自动化.txt'
fs=open(path,'w')
fs.write(u'东方头条%d'.encode('gbk')%random.randint(0,100))
fs.close()


