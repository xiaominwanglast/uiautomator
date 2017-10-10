#coding:utf-8
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
url='http://jira.dfshurufa.com/login.jsp'
#driver = webdriver.PhantomJS(executable_path="E:\\mac\\id\\phantomjs-2.1.1-windows\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")
driver=webdriver.Chrome()
driver.set_page_load_timeout(10)
driver.get(url)
driver.find_element_by_id('login-form-username').send_keys('wangxiaomin')
driver.find_element_by_id('login-form-password').send_keys('wang12345')
driver.find_element_by_id('login-form-submit').click()
time.sleep(2)
try:
    driver.get('http://jira.dfshurufa.com/issues/?jql=project%20%3D%20TTAND%20AND%20issuetype%20%3D%20%E7%BC%BA%E9%99%B7%20AND%20resolution%20%3D%20Unresolved%20ORDER%20BY%20priority%20DESC%2C%20updated')
    time.sleep(10)
    print driver.page_source.encode('gb18030')
    driver.quit()
except Exception as e:
    print e
    driver.quit()
