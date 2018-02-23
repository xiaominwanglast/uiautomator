#coding:utf-8

import sys
import time
import os

sys.path.append (r"..")

from apptest.PO import BasePage
from apptest.PO import DiscoveryPage
from apptest.PO import Superunit
from apptest.Public.getmethodname  import GetName
from apptest.Public.screenshot import screenshot
from apptest.Public.sendemail import smail
from apptest.PO import MinePage
from apptest.Public import processfile
from PIL import Image
class nologin_discovery(Superunit.initunit):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\nologin\\activity\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"
    screen=os.path.dirname(os.getcwd())+"\\screen\\nologin\\activity\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"
    body1=u"发现>活动>UI>未登录>UI检查-空白页"
    def test_01_activity(self):
        u"""活动商城H5页面UI测试"""
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        MinePage.Mine(self.driver).click_mine_entry()
        DiscoveryPage.Discovery(self.driver).click_foundentry()
        point=BasePage.Base(self.driver).tap(0.5,0.5,self.driver)
        processfile.testdirexists(self.screen)
        self.driver.get_screenshot_as_file(self.screen+"screen.png")
        daytime=Image.open(self.work_path+"screen.png").getpixel((point[0],point[1]))
        print daytime
        try:
            self.assertTrue(daytime[0] in [119,13,85,255])
            print (u"活动>UI>商城H5页面显示-空白页")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1,body=self.body1)
        except:
            pass





