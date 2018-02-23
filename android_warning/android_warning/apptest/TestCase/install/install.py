#coding:utf-8
import  unittest
import  time
import os
import sys

sys.path.append (r"..")
from apptest.PO.adbUtils import ADB
from apptest.PO import Superunit
from apptest.PO import BasePage
from apptest.PO import MinePage
from apptest.PO import SetPage
from apptest.Public.screenshot import screenshot
from apptest.Public.getmethodname import GetName
from apptest.Public import readconfig

class installApp(Superunit.initunit):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\install\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"
    install_path=os.path.dirname(os.getcwd())+"\\data\\touTiao_v1.5.5.apk"
    install_path1=os.path.dirname(os.getcwd())+"\\data\\touTiao_v1.5.6.apk"
    install_path2=os.path.dirname(os.getcwd())+"\\data\\touTiao_v1.5.7.apk"
    def test_01_install(self):
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        MinePage.Mine(self.driver).click_mine_entry()
        time.sleep(5)
        os.popen("adb install -r %s"%self.install_path)
        time.sleep(10)

    def test_02_install(self):
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        MinePage.Mine(self.driver).click_mine_entry()
        time.sleep(5)
        os.popen("adb install -r %s"%self.install_path1)
        time.sleep(10)

    def test_03_install(self):
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        MinePage.Mine(self.driver).click_mine_entry()
        time.sleep(5)
        os.popen("adb install -r %s"%self.install_path2)
        time.sleep(10)

    def test_04_uninstall(self):
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        MinePage.Mine(self.driver).click_mine_entry()
        time.sleep(5)
        os.popen("adb shell pm uninstall -k %s"%readconfig.readappconfig()[0])
        time.sleep(10)

if __name__=="__main__":
    unittest.main()