#coding:utf-8
import  unittest

import os
import time
import nologin_testVideo

class defpath(object):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\login\\video\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"
class login_videos(nologin_testVideo.nologin_video):
    work_path=defpath.work_path
    body1=u"视频>新闻信息流>UI>已登录>UI检查-空白页"
    body2=u"视频>视频内页>UI>已登录>UI检查-空白页"





