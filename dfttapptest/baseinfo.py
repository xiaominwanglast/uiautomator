#coding:utf-8
import  time,unittest
from appium import webdriver
import random
from selenium.webdriver.support.ui import WebDriverWait
class baseinfo(unittest.TestCase):
    def setUp(self):
        desired_cups={}
        desired_cups['platformName']='Android'
        desired_cups['platformVersion']='7.0'
        desired_cups['deviceName']='F8UDU15214030172'
        desired_cups['appPackage']='com.tencent.mm'
        desired_cups['appActivity']='com.tencent.mm.ui.LauncherUI'
        #com.jifen.qukan  com.jifen.qukan.view.activity.JumpActivity
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_cups)
        time.sleep(10)
    def tearDown(self):
        self.driver.quit()
    def test_01_click(self):
        self.driver.find_element_by_xpath("//android.widget.LinearLayout[@index='11']").click()
        while True:
            try:
                ele=self.driver.find_elements_by_id('com.tencent.mm:id/a6r')
                ele[random.randint(0,len(ele)-1)].click()
                time.sleep(5)
                self.driver.find_element_by_xpath("//android.widget.TextView[@content-desc='更多']").click()
                self.driver.find_element_by_name(u'发送给朋友').click()
                WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id('com.tencent.mm:id/jd').is_displayed())
                self.driver.find_element_by_name('auto').click()
                WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id('com.tencent.mm:id/ad8').is_displayed())
                self.driver.find_element_by_name(u'发送').click()
                self.driver.find_element_by_id('com.tencent.mm:id/h4').click()
            except:
                try:
                    self.driver.find_element_by_xpath("//android.widget.TextView[@content-desc='更多']").click()
                    self.driver.find_element_by_name(u'发送给朋友').click()
                    WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id('com.tencent.mm:id/jd').is_displayed())
                    self.driver.find_element_by_name('auto').click()
                    WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id('com.tencent.mm:id/ad8').is_displayed())
                    self.driver.find_element_by_name(u'发送').click()
                    self.driver.find_element_by_id('com.tencent.mm:id/h4').click()
                except:
                    pass
                try:
                    self.driver.find_element_by_name(u'发送给朋友').click()
                    WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id('com.tencent.mm:id/jd').is_displayed())
                    self.driver.find_element_by_name('auto').click()
                    WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id('com.tencent.mm:id/ad8').is_displayed())
                    self.driver.find_element_by_name(u'发送').click()
                    self.driver.find_element_by_id('com.tencent.mm:id/h4').click()
                except:
                    pass
                try:
                    self.driver.find_element_by_name('auto').click()
                    WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id('com.tencent.mm:id/ad8').is_displayed())
                    self.driver.find_element_by_name(u'发送').click()
                    self.driver.find_element_by_id('com.tencent.mm:id/h4').click()
                except:
                    pass
                try:
                    self.driver.find_element_by_name(u'发送').click()
                    self.driver.find_element_by_id('com.tencent.mm:id/h4').click()
                except:
                    pass
                try:
                    self.driver.find_element_by_id('com.tencent.mm:id/h4').click()
                except:
                    pass
        '''
        self.driver.find_element_by_id('com.jifen.qukan:id/amain_btn_person').click()
        time.sleep(3)
        self.driver.tap([(500,1575)],500)
        time.sleep(3)
        self.driver.tap([(500,1525)],500)
        time.sleep(5)
        while True:
            try:
                self.driver.tap([(500,800)],500)
                WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id('com.tencent.mm:id/jd').is_displayed())
                self.driver.find_element_by_id('com.tencent.mm:id/jd').click()
                WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id('com.tencent.mm:id/ad8').is_displayed())
                self.driver.find_element_by_id('com.tencent.mm:id/ad8').click()
                WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id('com.tencent.mm:id/ad7').is_displayed())
                self.driver.find_element_by_id('com.tencent.mm:id/ad7').click()
                WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id('com.jifen.qukan:id/text_title').is_displayed())
            except:
                try:
                    self.driver.find_element_by_id('com.tencent.mm:id/h4').click()
                    WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id('com.jifen.qukan:id/text_title').is_displayed())
                except:
                    pass
                try:
                    self.driver.find_element_by_id('com.tencent.mm:id/ad8').click()
                    time.sleep(1)
                    self.driver.find_element_by_id('com.tencent.mm:id/ad7').click()
                    WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id('com.jifen.qukan:id/text_title').is_displayed())
                except:
                    pass
                    '''
if __name__=="__main__":
    unittest.main()