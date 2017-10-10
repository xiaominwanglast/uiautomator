#coding:utf-8
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait

def deal_tower_data():
    list_tower=[]
    sum=0
    html=get_tower_data()
    for i in range(2):
        if html=='request time_out':
            html=get_tower_data()
        else:
            break
    if html!='request time_out':
        soup=BeautifulSoup(html,'lxml')
        todo=soup.find_all('div',class_='todo-wrap')
        for data in todo:
            dit_data={}
            tower=data.find('span',class_='raw').string.strip()
            name=data.find('span',class_='assignee').string.strip()
            if data.find('span',class_='due'):
                finish_time=data.find('span',class_='due').string.strip()
            else:
                finish_time='not_sure'
            dit_data['tower']=tower
            dit_data['name']=name
            dit_data['finish_time']=finish_time
            list_tower.append(dit_data)
        html=''
        for i in list_tower:
         #   print type(i['finish_time'])
            if i['finish_time']==u'今天':
                sum+=1
                html=html+'*'+i['finish_time']+'\t'+i['name']+'\t'+i['tower']+'\n'
        if sum==0:
            return None
        else:
            return u'[tower今日任务提醒]'+'\n'+html
    else:
        return None

def get_tower_data():
    driver = webdriver.PhantomJS(executable_path="E:\\mac\\id\\phantomjs-2.1.1-windows\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")
    try:
        driver.set_page_load_timeout(10)
        url='https://tower.im/users/sign_in'
        driver.get(url)
        driver.find_element_by_id('email').send_keys('wangxiaomin@021.com')
        driver.find_element_by_name('password').send_keys('992623Wang')
        driver.find_element_by_id('btn-signin').click()
        WebDriverWait(driver, 6).until(lambda driver: driver.find_element_by_css_selector('.project.c5.i23').is_displayed())
        driver.find_element_by_css_selector('.project.c5.i23').click()
        WebDriverWait(driver, 6).until(lambda driver: driver.find_element_by_css_selector('.content-linkable').is_displayed())
        time.sleep(2)
        text=driver.page_source
        driver.quit()
        return text
    except:
        driver.quit()
        return 'request time_out'
if __name__=="__main__":
    print deal_tower_data()
