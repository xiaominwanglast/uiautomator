#coding:utf-8
import time
import sys
from selenium.webdriver.support.ui import WebDriverWait
sys.path.append (r'..')
from apptest.Public import readconfig

class Base (object):
    driver=None
    capabilities={'platformName':'Android',
                  'platformVersion':'4.4.4',
                  'UDID':'7b24ece4',
                  'deviceName':'7b24ece4',
                  'newCommandTimeout':1260,
                  'unicodeKeyboard':True,
                  'resetKeyboard':True,
                  'appPackage':readconfig.readappconfig()[0],
                  'appActivity':readconfig.readappconfig()[1]
    }

    def  __init__(self,appium_driver):

        self.driver=appium_driver
 #       self.capabilities['UDID']=appium_udid
 #       self.capabilities['deviceName']=appium_udid
        time.sleep(10)

    def find_element(self,*loc):
#        return self.driver.find_element(*loc)
        try:
            #确保元素是可见的。
            #注意：以下入参为元组的元素，需要加*。Python存在这种特性，就是将入参放在元组里。
#            WebDriverWait(self.driver,10).until(lambda driver: driver.find_element(*loc).is_displayed())
            #注意：以下入参本身是元组，不需要加*
#            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)

        except:
            time.sleep(5)
            try:
                self.driver.find_element_by_id("%s:id/btn_cancel"%Base.capabilities['appPackage']).click()
            except:
                pass
            try:
                self.driver.find_element_by_id("%s:id/close"%Base.capabilities['appPackage']).click()
            except:
                pass
            return self.driver.find_element(*loc)

    def find_elements(self,*loc):
#        return self.driver.find_element(*loc)
        try:
            #确保元素是可见的。
            #注意：以下入参为元组的元素，需要加*。Python存在这种特性，就是将入参放在元组里。
            WebDriverWait(self.driver,10).until(lambda driver: driver.find_element(*loc).is_displayed())
            #注意：以下入参本身是元组，不需要加*
#            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_elements(*loc)
        except:
            time.sleep(5)
            try:
                self.driver.find_element_by_id("%s:id/btn_cancel"%Base.capabilities['appPackage']).click()
            except:
                pass
            try:
                self.driver.find_element_by_id("%s:id/close"%Base.capabilities['appPackage']).click()
            except:
                pass
            return self.driver.find_elements(*loc)

    def do_swipe(self,driver,driection):
        self.driver=driver
        self.driection=driection

        window = self.driver.get_window_size()
        width = int(window[u'width'])
        height = int(window[u'height'])

        switcher={
            "up":lambda :self.driver.swipe(width /2, height * 3/4, width /2, height * 1/4, 1000),
            "smallup":lambda :self.driver.swipe(width /2, height * 3/5, width /2, height * 1/5, 1000),
            "bigup":lambda :self.driver.swipe(width /2, height * 7/10, width /2, height * 1/5, 1000),
            "down":lambda :self.driver.swipe(width / 2, height * 1 / 4, width / 2, height * 3 / 4, 1000),
            "left":lambda :self.driver.swipe(width * 5 / 6, height / 2, width * 1 / 6, height / 2, 1000),
            "right":lambda :self.driver.swipe(width * 1 / 6, height / 2, width * 5 / 6, height / 2, 1000)

        }
 #       print (self.driection)
#        func = switcher.get(driection)
        return switcher.get(driection)()

    def tapxy (self,x,y,driver,stime):
        self.driver=driver
        self.stime=stime
        self.x=x
        self.y=y
        window = self.driver.get_window_size()
        width = int(window[u'width'])
        height = int(window[u'height'])

        self.driver.tap([(int(self.x*width),int(self.y*height))],500)
        time.sleep(self.stime)

#readmsg()
    def tap(self,x,y,driver):
        self.driver=driver
        self.x=x
        self.y=y
        window = self.driver.get_window_size()
        width = int(window[u'width'])
        height = int(window[u'height'])
        return self.x*width,self.y*height

    def webstate(self):
        info = {0:"NO_CONNECTION",
        1:"AIRPLANE_MODE",
        2:"WIFI_ONLY",
        4:"DATA_ONLY",
        6:"ALL_NETWORK_ON"}

        stat = self.driver.network_connection
        return info.get(stat)