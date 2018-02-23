#coding:utf-8


from adbUtils import ADB
from movement import Closement
import os

from BasePage import Base
from appium import webdriver

def testinstall(packname,installname):
    #获取adb连接,单个设备可以不传该参数
    adb = ADB()

#    os.popen("taskkill /im   adb.exe /f")
#    time.sleep(2)
    #获取设备信息

  #  print "设备序列号: ".decode("utf-8") + adb.getDeviceID()
 #   print "设备状态： ".decode("utf-8") + adb.getDeviceState()
  #  print "设备屏幕分辨率: ".decode("utf-8") + str(adb.getScreenResolution())
   # print "设备电池状态： ".decode("utf-8") + adb.getBatteryStatus()
#    print "设备电池温度： ".decode("utf-8") + str(adb.getBatteryTemp())
  #  print "设备电池电量： ".decode("utf-8") + str(adb.getBatteryLevel())


    #安装data目录下的apk

    if(not adb.isInstall(packname)):
        print (u"---------------------------------安装中---------------------------------")
        str1= os.path.dirname(os.getcwd())+"\\data\\"+installname
        os.popen('adb install %s'%str1)
        adb.shell("sleep 15")
        print (u"---------------------------------安装成功------------------------------------")

    elif(not adb.getAppVersion(packname)):
        print (u"----------------------------------安装中-------------------------------------")
        #应用不存在则安装
#        print adb.installApp(os.path.dirname(os.getcwd())+"\\data\\"+installname)
        str1= os.path.dirname(os.getcwd())+"\\data\\"+installname
        os.popen('adb  install %s '%str1)

#        print 'install status : %s' % output.read()
#        time.sleep(15)
        adb.shell("sleep 15")
        print (u"---------------------------------安装成功------------------------------------")

    else:
        print u"手机上的APP版本号为%s"%adb.getAppVersion(packname)


def testwifi(adb):

    if (adb.shell(" dumpsys wifi|findstr \"CONNECTED\/CONNECTED\" ").stdout.read().strip()==''):

         return ("network not connect")

 #       print ("netrork connect,network's message:%"%str2)
    else:
        print (("network connect's message:")+adb.shell(" dumpsys wifi|findstr \"CONNECTED\/CONNECTED\" ").stdout.read().strip())

