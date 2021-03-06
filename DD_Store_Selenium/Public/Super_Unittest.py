#coding:utf-8
import time
import os
import json
from selenium import webdriver
from unittest import TestCase
class SuperUnit(TestCase):

    mainGoodId=125767  #价格75,无活动
    zengDouGoodId=125801  #价格80，赠豆4元
    manJianGoodId=125802   #价格100 ，满50减10
    manZengGoodId=125804   #价格150 ，赠125805 一个
    ZGoodId=125805     #满300赠的非卖品
    ZGoodIdCount = 1 # 满300赠的非卖品
    heikaGoodId=125811   #价格100 ，黑卡活动，除了赠豆不享受其他优惠
    heikaZendDouGoodId=125857  #价格100，黑卡活动，赠豆5元
    heikaTJGoodId=125861     #原价120，现价100
    weihuoGoodId=125822  #价格30，尾货闪销
    manJianGoodIdTD=125845  #价格100 ，多梯度满减 满100减10，200减25，300减40

    @property
    def store_username(self):
        return self.load_json()['storePhoneNum']

    @property
    def store_Pwd(self):
        return self.load_json()['storePwd']

    @classmethod
    def load_json(cls):
        with open(os.path.dirname(os.getcwd()) + '\\Settings\\storeInfo.json', 'r') as load_f:
            load_json = json.load(load_f)
        return load_json

    @classmethod
    def setUpClass(cls):
        #初始化webdriver
        cls.driver=webdriver.Firefox(executable_path=r'C:\Python27\geckodriver.exe',log_path=os.path.dirname(os.getcwd())+'\\TestLog\\geckodriver.log')
        cls.driver.maximize_window()
        time.sleep(2)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    #TODO 启动3次网址
    def openUrl(self,url):
        for run_time in range(3):
            try:
                self.driver.set_page_load_timeout(15)
                self.driver.get(url=url)
                break
            except Exception as e:
                print e

    #TODO 截取上下全图
    def screenShot(self,path):
        self.driver.get_screenshot_as_file(path)


