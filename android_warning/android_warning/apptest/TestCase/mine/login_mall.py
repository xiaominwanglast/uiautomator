#coding:utf-8
import sys
import time
import os
sys.path.append (r"..")
from apptest.TestCase.mine import nologin_mall

class depath(object):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\login\\mall\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"
class login_mall(nologin_mall.mallUI):
    work_path=depath.work_path
    body1=u"我的>商城>UI>已登录>检查UI-空白页"