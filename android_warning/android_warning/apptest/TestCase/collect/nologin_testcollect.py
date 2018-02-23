#coding:utf-8

import os
import time
from apptest.TestCase.collect import login_testcollect
class defpath(object):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\nologin\\collect\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"
class nologin_test_collect(login_testcollect.login_Collect):
    work_path=defpath.work_path
    body1 =u"我的>收藏>UI>未登录>UI检查-空白页"
