#coding:utf-8
import sys
import time
import os
sys.path.append (r"..")
from apptest.TestCase.mine import mesg_test

class depath(object):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\login\\mesg\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"
class login_mesg(mesg_test.mesg):
    work_path=depath.work_path
    body1=u"我的>消息中心>UI>已登录>UI检查-空白页"