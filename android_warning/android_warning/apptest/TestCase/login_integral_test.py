#coding:utf-8

import random
import os ,time
from apptest.TestCase import nologin_integral_test

class depath(object):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\nologin\\integral\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"

class login_tel_integral(nologin_integral_test.nologin_points):
    work_path=depath.work_path

class login_QQ_integral(login_tel_integral):
    pass

class login_weibo_integral(login_tel_integral):
    pass

class login_weixin_integral(login_tel_integral):
    pass


