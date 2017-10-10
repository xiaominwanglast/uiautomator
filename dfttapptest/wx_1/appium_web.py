#coding:utf-8
import requests
import sys
reload(sys)
sys.setdefaultencoding='gbk'
session=requests.Session()
ul=session.get('http://www.baidu.com')
print ul.text.encode('gb18030')
