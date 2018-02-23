#coding:utf-8
import  unittest
import os
import time
from apptest.TestCase.mine import task_dailyUI

class defpath(object):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\login\\taskcenter\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"
class login_taskcenterUI(task_dailyUI.UItask):
    work_path=defpath.work_path
    body1=u"我的>任务中心>UI>已登录>UI检查-空白页"