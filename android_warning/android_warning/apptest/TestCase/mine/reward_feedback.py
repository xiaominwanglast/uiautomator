#coding:utf-8

from apptest.PO import Superunit
from apptest.PO import MinePage
from apptest.Public.getmethodname import GetName
from apptest.PO import BasePage
from apptest.Public.screenshot import screenshot
from apptest.Public.sendemail import smail
import os ,time
from apptest.PO import feedback

class rewardfeedback(Superunit.initunit):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\mine\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"
    body1=u"我的>有奖反馈>UI>未登录>UI检查-空白页"
    def test_01_feedback(self):
        u"""有奖反馈UI测试"""
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        MinePage.Mine(self.driver).click_mine_entry()
        BasePage.Base(self.driver).do_swipe(self.driver,"up")
        time.sleep(4)
        MinePage.Mine(self.driver).click_feedback()
        try:
            self.assertTrue(feedback.feed(self.driver).find_kefutext())
        except:
            print (u"有奖反馈>UI>UI检查-空白页")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1,body=self.body1)