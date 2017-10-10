#coding:utf-8
from selenium import webdriver
import re
js_total=0
count=0
def run(url,data):
    global js_total
    driver=webdriver.PhantomJS(executable_path="E:\\mac\\id\\phantomjs-2.1.1-windows\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe") #webdiver加载phantomjs驱动
    driver.set_page_load_timeout(20)
    try:
        driver.get(url)
        html=driver.page_source
        if re.findall(data,html):
            js_total+=1
        driver.quit()
    except:
        driver.quit()
        run(url,data)
def main():
    global count
    workpath='log.txt'
    with open(workpath,'rb') as fs:
        txt=fs.readlines()
    url=txt[1].strip()
    count=int(txt[0].strip())
    panduan=txt[2].strip()
    print u'测试链接为%s'%url
    print u'测试次数为%d'%count
    print u'判断测试链路js(取?后内容)%s'%panduan
    print u'***'*20
    print u'正在测试······'
    for i in range(count):
        if i%10==0 and i!=0:
            print u'目前测试次数为%d'%i,u'出现js流次数为%d'%js_total
        run(url,panduan)
main()
print u'***'*8+u'结论'+u'***'*8
print u'测试次数为%d'%count, u'出现js流次数为%d'%js_total