#coding:utf-8
import sys
import time
import os
sys.path.append (r"..")
from apptest.TestCase.mine import offline_downloadnews

class depath(object):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\login\\offline\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"
class login_offlinedownUI(offline_downloadnews.dlnews):
    work_path=depath.work_path
    body1=u"我的>离线阅读>UI>已登录>UI检查-空白页"