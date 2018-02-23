#coding:utf-8

from apptest.PO import Superunit
from apptest.PO import  BasePage
from apptest.PO import  MinePage
from apptest.Public.getmethodname import GetName
from apptest.Public.screenshot import screenshot
from apptest.Public.sendemail import smail
import os ,time
from PIL import Image
from apptest.Public import processfile
class nightmode(Superunit.initunit):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\mine\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"
    screen=os.path.dirname(os.getcwd())+"\\screen\\mine\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"
    def test_01_night(self):
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        MinePage.Mine(self.driver).click_mine_entry()
        BasePage.Base(self.driver).do_swipe(self.driver,"up")
        time.sleep(5)
        point=BasePage.Base(self.driver).tap(0.5,0.5,self.driver)
        processfile.testdirexists(self.screen)
        self.driver.get_screenshot_as_file(self.screen+"screen.png")
        daytime=Image.open(self.work_path+"screen.png").getpixel((point[0],point[1]))
        print daytime
        MinePage.Mine(self.driver).click_night()
        processfile.testdirexists(self.screen)
        self.driver.get_screenshot_as_file(self.screen+"screen.png")
        night=Image.open(self.work_path+"screen.png").getpixel((point[0],point[1]))
        print night
        time.sleep(2)
        MinePage.Mine(self.driver).click_night()
        try:
            self.assertNotEqual(daytime[0],night[0])
            self.assertEqual(night[0],21)
            self.assertEqual(night[1],21)
            self.assertEqual(night[2],21)
        except:
            print (u"夜间模式>夜间&日间模式切换-异常")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body=u"夜间模式>夜间&日间模式切换-异常"
            smail().send_errormsg(str(filename),body,self.work_path)