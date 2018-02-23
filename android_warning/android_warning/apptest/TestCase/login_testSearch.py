#coding:utf-8

import nologin_testSearch
import os
import time
import unittest

class depath(object):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\login\\search\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"
class login_search(nologin_testSearch.nologin_serach):
    work_path=depath.work_path
    body1=u"搜索>悬窗搜索>UI>已登录>UI检查-空白页"
    body2=u'搜索>悬窗搜索输入内容>UI>已登录>UI检查-空白页'
