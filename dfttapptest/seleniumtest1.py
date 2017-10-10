#coding:utf-8
from selenium import webdriver
from selenium.webdriver import ActionChains
import time
def test():
    driver=''
    try:
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
        driver = webdriver.Chrome(chrome_options=options)
    except Exception,e:
        print e
    try:
        driver.set_page_load_timeout(20)
        driver.get('http://www.baidu.com')
        el=driver.find_element_by_css_selector('a.pf')
        ActionChains(driver).move_to_element(el).perform()
        driver.find_element_by_xpath('//div/a[@class="setpref"]').click()
        time.sleep(5)
    except Exception,e:
        print e
    driver.quit()
test()