#coding:utf-8
import sys
import time
import os
sys.path.append (r"..")
from apptest.TestCase.mine import nologin_despoil

class depath(object):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\login\\despoil\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"
class login_despoil(nologin_despoil.despoilUI):
    work_path=depath.work_path
    body1=u"我的>夺宝>UI>已登录>检查UI-无夺宝功能"
    body2=u"我的>夺宝>UI>已登录>检查UI-空白页"