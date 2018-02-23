#coding:utf-8
import time
import os
import sys
sys.path.append(r'..')

from apptest.PO import CollectPage
from apptest.PO import Superunit
from apptest.Public.getmethodname import GetName
from apptest.Public.screenshot import screenshot
from apptest.Public.sendemail import smail


class login_Collect(Superunit.initunit):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\login\\collect\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"
    body1=u"我的>收藏>UI>已登录>UI检查-空白页"
    def test_01_collect(self):
        u"""收藏界面UI测试"""
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        CollectPage.Collect(self.driver).click_mine()
        CollectPage.Collect(self.driver).click_mine_collect()
        try:
            self.assertTrue(CollectPage.Collect(self.driver).find_tv_text())
            self.assertTrue(CollectPage.Collect(self.driver).find_tv_video())
        except:
            print (u"收藏>UI>UI检查-空白页")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1,body=self.body1)





