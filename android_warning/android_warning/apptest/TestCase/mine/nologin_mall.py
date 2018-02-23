#coding:utf-8
from apptest.PO import Superunit
from apptest.PO import MinePage
from apptest.Public.getmethodname import GetName
from apptest.Public.screenshot import screenshot
from apptest.Public.sendemail import smail
import os ,time

class mallUI(Superunit.initunit):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\nologin\\mall\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"
    body1=u"我的>商城>UI>未登录>检查UI-空白页"
    def test_01_UI(self):
        u"""我的钱包UI检查测试"""
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        MinePage.Mine(self.driver).click_mine_entry()
        MinePage.Mine(self.driver).click_mall()
        try:
            self.assertTrue(MinePage.Mine(self.driver).find_malltitle())
        except:
            print (u"商城>UI>检查UI-空白页")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1,body=self.body1)

