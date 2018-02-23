#coding:utf-8
import sys
import time
import os
sys.path.append (r"..")
from apptest.TestCase import tuisong

class depath(object):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\login\\despoil\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"
class login_tuisong(tuisong.Tuisong):
    work_path=depath.work_path
    body1=u"我的>推送新闻>UI>已登录>UI检查-空白页"

