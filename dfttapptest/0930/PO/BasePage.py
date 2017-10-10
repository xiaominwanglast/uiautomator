#coding:utf-8
import time
from appium import  webdriver
from selenium.webdriver.common.by import  By
import ConfigParser
import os
import sys

def readmsg():
    config = ConfigParser.ConfigParser()

    with open(os.path.dirname(os.getcwd())+"\\config\\appconfig.ini","r") as cfgfile:
        config.readfp(cfgfile)
        packname=config.get("app","packname")
        appActivity=config.get("app","appActivity")


#    print smtpHost,smtpPort,sslPort,fromMail,username,password,toMail,cc
    return packname,appActivity


class Base (object):
    driver=None
    capabilities={'platformName':'Android',
                  'platformVersion':'4.4.4',
                  'deviceName':'172.18.14.201:5555',
                  'unicodeKeyboard':True,
                  'resetKeyboard':True,
                  'appPackage':readmsg()[0],
                  'appActivity':readmsg()[1]

    }

    def  __init__(self,appium_driver):
        self.driver=appium_driver
        time.sleep(10)


    def find_element(self,*loc):
#        return self.driver.find_element(*loc)
        try:
            #确保元素是可见的。
            #注意：以下入参为元组的元素，需要加*。Python存在这种特性，就是将入参放在元组里。
#            WebDriverWait(self.driver,10).until(lambda driver: driver.find_element(*loc).is_displayed())
            #注意：以下入参本身是元组，不需要加*
#            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))

#            print self.driver.find_element(*loc)
            return self.driver.find_element(*loc)
        except:
            print u"%s 页面中未能找到 %s 元素"%(self, loc)



#滑动页面的优化版本

    def do_swipe(self,driver,driection):
        self.driver=driver
        self.driection=driection

        window = self.driver.get_window_size()
        width = int(window[u'width'])
        height = int(window[u'height'])

        switcher={
            "up":lambda :self.driver.swipe(width /2, height * 3/4, width /2, height * 1/4, 1000),
            "down":lambda :self.driver.swipe(width / 2, height * 1 / 4, width / 2, height * 3 / 4, 1000),
#            "down":lambda :3,
            "left":lambda :self.driver.swipe(width * 5 / 6, height / 2, width * 1 / 6, height / 2, 1000),
            "right":lambda :self.driver.swipe(width * 1 / 6, height / 2, width * 5 / 6, height / 2, 1000)

        }
 #       print (self.driection)
        func = switcher.get(driection)
        return func()




#readmsg()
