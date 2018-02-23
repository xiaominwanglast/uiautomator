#coding:utf-8
import  unittest
import  time
import os
import sys
from apptest.Public import readconfig
sys.path.append (r"..")
from apptest.PO.adbUtils import ADB
from apptest.PO import Superunit
from apptest.PO import BasePage
from apptest.PO import MinePage
from apptest.PO import SetPage
from apptest.Public.screenshot import screenshot
from apptest.Public.sendemail import smail
from appium.webdriver.common.touch_action import TouchAction
from apptest.Public.getmethodname import GetName

class uninstallApp(Superunit.initunit):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\install\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"
    install_path=os.path.dirname(os.getcwd())+"\\data\\touTiao_v1.5.5.apk"
    def test_01_uninstall(self):
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        print(u"准备卸载app")
        time.sleep(5)
        os.popen("adb shell pm uninstall -k %s"%readconfig.readappconfig()[0])
        try:
            self.assertFalse(ADB().isInstall(readconfig.readappconfig()[0]))
            print (u"卸载成功")
        except:
            print (u"卸载版本号失败")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body1=u"卸载版本号失败"
      #      smail().send_errormsg(str(filename),body1,self.work_path)
        else:
            os.popen("adb install -r %s"%self.install_path)
            if ADB().isInstall(readconfig.readappconfig()[0])==True:
                print (u"版本正确安装")
            else:
                print (u"版本安装失败")
                filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                body1=u"版本安装失败"
        #    smail().send_errormsg(str(filename),body1,self.work_path)


if __name__=="__main__":
    unittest.main()