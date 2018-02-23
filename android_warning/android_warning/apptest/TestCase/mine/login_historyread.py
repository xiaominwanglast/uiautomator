#coding:utf-8
import sys
import time
import os
sys.path.append (r"..")
from apptest.TestCase.mine import history_read

class depath(object):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\login\\historyread\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"
class login_historyreadUI(history_read.hisread):
    work_path=depath.work_path
    body1=u"我的>历史阅读>UI>已登录>UI检查-空白页"