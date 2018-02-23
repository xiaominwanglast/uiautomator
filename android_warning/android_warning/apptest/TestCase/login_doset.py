#coding:utf-8
import sys
import time
import os
sys.path.append (r"..")
import dologout

class depath(object):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\login\\offline\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"
class login_setUI(dologout.setUI):
    work_path=depath.work_path
    body1=u"我的>设置>UI>已登录>UI检查-空白页"