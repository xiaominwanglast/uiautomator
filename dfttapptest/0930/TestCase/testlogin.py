#coding:utf-8
import  unittest
import  time
from appium import  webdriver
from ddt import ddt,data,unpack
import csv
import sys

sys.path.append (r"..")

from PO import BasePage
from PO import LoginPage



def get_csv_data(file_name):
    rows = []
    data_file = open(file_name, "rb")
    reader = csv.reader(data_file)
    next(reader, None)
    for row in reader:
        rows.append(row)
    return rows



@ddt
class login (unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',BasePage.Base.capabilities)
#        self.username="13554736037"
#        self.password="111111"
        time.sleep(10)

    @data(*get_csv_data(r"d:\logindata.csv"))

    @unpack

    def test_01_login(self,username,password):
#        self.driver.find_element(By.ID,"com.songheng.eastnews:id/rb_bottom_mine").click()

        LoginPage.Login(self.driver).dologout()
        time.sleep(2)

        LoginPage.Login(self.driver).input_mine()


        BasePage.Base(self.driver).do_swipe(self.driver,"down")

        LoginPage.Login(self.driver).input_nologin()

        LoginPage.Login(self.driver).input_username(username)

        LoginPage.Login(self.driver).input_password(password)

        LoginPage.Login(self.driver). click_submit()

        time.sleep(5)
#        Login(self).input_mine()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()


