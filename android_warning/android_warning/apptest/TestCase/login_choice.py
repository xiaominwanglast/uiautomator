#coding:utf-8

import sys
import time
import os
sys.path.append (r"..")

from apptest.TestCase import nologin_choice


class depath(object):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\nologin\\choice\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"

class login_tel_choice(nologin_choice.nologin_choice):
    work_path=depath.work_path

class login_QQ_choice(login_tel_choice):
    pass

class login_weibo_choice(login_tel_choice):
    pass

class login_weixin_choice(login_tel_choice):
    pass



