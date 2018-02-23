#coding:utf-8
import  unittest
import os
import time
import nologin_channelUI

class defpath(object):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\login\\channel\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"
class login_channel(nologin_channelUI.nologin_channelUI):
    work_path=defpath.work_path
    body1=u"新闻>新闻频道管理>UI>已登录>UI检查-空白页"