#coding:utf-8
import  time,unittest,os,xlrd
from appium import webdriver
import random
from selenium.webdriver.support.ui import WebDriverWait
class baseinfo(unittest.TestCase):
    def setUp(self):
        #检测appium是否已经开启
        if not os.popen('netstat -ano|findstr 4723|findstr LISTENING').read():
            os.system("start /b appium --address 127.0.0.1 --port 4723")
            #taskkill /pid %s /f
            time.sleep(8)
        desired_cups={}
        desired_cups['platformName']='Android'
        desired_cups['platformVersion']='7.0'
        desired_cups['deviceName']='F8UDU15214030172'
        desired_cups['appPackage']='com.tencent.mm'
        desired_cups['appActivity']='com.tencent.mm.ui.LauncherUI'
        #com.jifen.qukan  com.jifen.qukan.view.activity.JumpActivity
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_cups)
        time.sleep(15)
    def tearDown(self):
        self.driver.quit()
    def test_01_click(self):
        work_path=os.path.dirname(os.getcwd())+'\\wx_1\\Test_url.xls'
        self.driver.find_element_by_xpath("//android.widget.LinearLayout[@index='10']").click()
        wk=xlrd.open_workbook(work_path)
        sheet=wk.sheet_by_name('Sheet1')
        for i in range(1,sheet.nrows):
            while True:
                try:
                    testurl_ele=self.driver.find_elements_by_id('com.tencent.mm:id/ij')
                    share_ele=self.driver.find_elements_by_id('com.tencent.mm:id/a80')
                    self.assertTrue(testurl_ele[len(testurl_ele)-1].location['y']>share_ele[len(share_ele)-1].location['y'])
                except:
                    continue
                else:
                    try:
                        ele=self.driver.find_elements_by_id('com.tencent.mm:id/ij')
                        ele[len(ele)-1].click()
                        time.sleep(5)
                        self.driver.find_element_by_xpath("//android.widget.TextView[@content-desc='更多']").click()
                        self.driver.find_element_by_name(u'发送给朋友').click()
                        WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id('com.tencent.mm:id/ja').is_displayed())
                        self.driver.find_element_by_name('auto').click()
                        WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id('com.tencent.mm:id/aes').is_displayed())
                        self.driver.find_element_by_name(u'发送').click()
                        self.driver.find_element_by_id('com.tencent.mm:id/h7').click()
                    except:
                        try:
                            self.driver.find_element_by_xpath("//android.widget.TextView[@content-desc='更多']").click()
                            self.driver.find_element_by_name(u'发送给朋友').click()
                            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id('com.tencent.mm:id/ja').is_displayed())
                            self.driver.find_element_by_name('auto').click()
                            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id('com.tencent.mm:id/aes').is_displayed())
                            self.driver.find_element_by_name(u'发送').click()
                            self.driver.find_element_by_id('com.tencent.mm:id/h7').click()
                        except:
                            pass
                        try:
                            self.driver.find_element_by_name(u'发送给朋友').click()
                            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id('com.tencent.mm:id/ja').is_displayed())
                            self.driver.find_element_by_name('auto').click()
                            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id('com.tencent.mm:id/aes').is_displayed())
                            self.driver.find_element_by_name(u'发送').click()
                            self.driver.find_element_by_id('com.tencent.mm:id/h7').click()
                        except:
                            pass
                        try:
                            self.driver.find_element_by_name('auto').click()
                            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id('com.tencent.mm:id/aes').is_displayed())
                            self.driver.find_element_by_name(u'发送').click()
                            self.driver.find_element_by_id('com.tencent.mm:id/h7').click()
                        except:
                            pass
                        try:
                            self.driver.find_element_by_name(u'发送').click()
                            self.driver.find_element_by_id('com.tencent.mm:id/h7').click()
                        except:
                            pass
                        try:
                            self.driver.find_element_by_id('com.tencent.mm:id/h7').click()
                        except:
                            pass
                    break

if __name__=="__main__":
    unittest.main()