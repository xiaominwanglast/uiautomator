#coding:utf-8
import  unittest
import os
import time
import nologin_testnews

class defpath(object):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\login\\news\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"
class login_news(nologin_testnews.nologin_news):
    work_path=defpath.work_path
    body1=u"新闻>新闻信息流>UI>已登录>UI检查-空白页"
    body2=u"新闻>新闻内页>UI>已登录>UI检查-空白页"










