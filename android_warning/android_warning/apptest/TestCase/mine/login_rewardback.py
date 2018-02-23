#coding:utf-8
import sys
import time
import os
sys.path.append (r"..")
from apptest.TestCase.mine import reward_feedback

class depath(object):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\login\\rewardback\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"
class login_rewardbackUI(reward_feedback.rewardfeedback):
    work_path=depath.work_path
    body1=u"我的>有奖反馈>UI>已登录>UI检查-空白页"