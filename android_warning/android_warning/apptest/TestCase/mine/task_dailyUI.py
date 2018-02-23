#coding:utf-8

from apptest.PO import Superunit
from apptest.PO import  TaskCenterPage
from apptest.PO import  BasePage
from apptest.PO import  MinePage
from apptest.Public.getmethodname import GetName
from apptest.Public.screenshot import screenshot
from apptest.Public.sendemail import smail
import os ,time

class UItask(Superunit.initunit):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\mine\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"
    body1=u"我的>任务中心>UI>未登录>UI检查-空白页"
    def test_01_taskUI(self):
        u"""任务中心UI检查测试"""
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        MinePage.Mine(self.driver).click_mine_entry()
        MinePage.Mine(self.driver).click_task()
        try:
            TaskCenterPage.taskcenter(self.driver).click_iv_close()
        except:
            pass
        try:
            self.assertTrue(TaskCenterPage.taskcenter(self.driver).find_tvdetails())
            self.assertTrue(TaskCenterPage.taskcenter(self.driver).find_sign_ele())
            self.assertTrue(TaskCenterPage.taskcenter(self.driver).find_tvtodaydate())
        except:
            print (u"任务中心>UI>UI检查-空白页")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1,body=self.body1)
