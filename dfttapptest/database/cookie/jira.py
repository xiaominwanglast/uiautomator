#coding:utf-8
import urllib
import requests
data={'os_username':'wangxiaomin',
      'os_password':'wang12345',
      'os_destination':'',
      'user_role':'',
      'atl_token':'',
      'login':'Log In'}
url='http://jira.dfshurufa.com/login.jsp'
session=requests.Session()
header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.6 Safari/537.36',}
session.post(url=url,headers=header,data=data,timeout=3)

rq=session.get('http://jira.dfshurufa.com/issues/?jql=project%20%3D%20TTAND%20AND%20issuetype%20%3D%20%E7%BC%BA%E9%99%B7%20AND%20status%20in%20(Open%2C%20Reopened)%20AND%20resolution%20%3D%20Unresolved%20ORDER%20BY%20priority%20DESC%2C%20updated%20DESC',headers=header)
print rq.text
