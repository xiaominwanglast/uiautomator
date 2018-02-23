#coding:utf-8
import  unittest
import time
import nologin_testdiscovery
import os

class defpath(object):
   work_path=os.path.dirname(os.getcwd())+"\\screen\\login\\activity\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"
   screen=os.path.dirname(os.getcwd())+"\\screen\\login\\activity\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"
class login_discovery(nologin_testdiscovery.nologin_discovery):
    work_path=defpath.work_path
    screen = defpath.screen
    body1=u"发现>活动>UI>已登录>UI检查-空白页"