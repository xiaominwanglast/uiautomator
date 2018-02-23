#coding:utf-8
import  unittest

import os
import time
import nologin_choice

class defpath(object):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\login\\choice\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"
class login_choice(nologin_choice.nologin_choice):
    work_path=defpath.work_path
    body1=u"发现>精选>UI>已登录>UI检查-空白页"