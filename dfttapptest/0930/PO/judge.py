#coding:utf-8


from adbUtils import ADB
from movement import Closement
import os
import time
from BasePage import Base
from appium import webdriver
import ConfigParser

def testinstall(packname,installname):
    #获取adb连接,单个设备可以不传该参数
    adb = ADB()

    #获取设备信息

    print "设备序列号: ".decode("utf-8") + adb.getDeviceID()
    print "设备状态： ".decode("utf-8") + adb.getDeviceState()
    print "设备屏幕分辨率: ".decode("utf-8") + str(adb.getScreenResolution())
    print "设备电池状态： ".decode("utf-8") + adb.getBatteryStatus()
    print "设备电池温度： ".decode("utf-8") + str(adb.getBatteryTemp())
    print "设备电池电量： ".decode("utf-8") + str(adb.getBatteryLevel())

    #安装data目录下的apk
    if(not adb.isInstall(packname)):
        print (u"-------------------------------------------------------安装中---------------------------------------------------------")
        #应用不存在则安装
#        print adb.installApp(os.path.dirname(os.getcwd())+"\\data\\"+installname)
        str1= os.path.dirname(os.getcwd())+"\\data\\"+installname
        output=os.popen('adb  install %s '%str1)
        print 'install status : %s' % output.read()
        time.sleep(15)
        print (u"-------------------------------------------------------安装成功---------------------------------------------------------")

        driver=webdriver.Remote('http://localhost:4723/wd/hub',Base.capabilities)

        Closement(driver).do_close()

        driver.quit()

    else:
        print u"手机上的APP版本号为%s"%adb.getAppVersion(packname)
#        print ("安装成功").decode("utf-8")
#    else:
        #存在则先卸载，后安装
#        adb.removeApp("com.songheng.eastnews")
#        print ("卸载成功").decode("utf-8")
#	time.sleep(5)
#        adb.installApp("f:\\apptest\\dftt1.4.3.apk")
#        print ("重新安装成功").decode("utf-8")


def testwifi(adb):

    if (adb.shell(" dumpsys wifi|findstr \"CONNECTED\/CONNECTED\" ").stdout.read().strip()==''):

         return ("network not connect")

 #       print ("netrork connect,network's message:%"%str2)
    else:
        print (("network connect's message:")+adb.shell(" dumpsys wifi|findstr \"CONNECTED\/CONNECTED\" ").stdout.read().strip())


if __name__=="__main__":
    testinstall("com.songheng.eastnews","touTiao_v1.4.7.apk")
