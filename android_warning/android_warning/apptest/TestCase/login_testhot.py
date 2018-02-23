#coding:utf-8

import nologin_testhot
import os
import time
import unittest
class defpath(object):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\login\\hot\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"
class login_hot(nologin_testhot.nologin_Hot):
    work_path=defpath.work_path
    body1=u"发现>热文>UI>已登录>UI检查-空白页"
    body2=u"发现>红人>UI>已登录>UI检查-空白页"
