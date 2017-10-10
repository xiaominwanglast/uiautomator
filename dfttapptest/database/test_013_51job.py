#coding:utf-8
import HTMLParser
from selenium import webdriver
import time,os,requests,xlwt,xlrd
from lxml import etree
from xlutils.copy import copy
from bs4 import  BeautifulSoup

def url_do(path,job):

    headers = { 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:51.0) Gecko/20100101 Firefox/51.0'}
    url='http://search.51job.com/jobsearch/advance_search.php'
    driver=webdriver.PhantomJS(executable_path="E:\\mac\\id\\phantomjs-2.1.1-windows\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")
    try:
        driver.set_page_load_timeout(10)
        driver.get(url)
        driver.find_element_by_id('kwdselectid').send_keys(job)
        driver.find_element_by_css_selector('.p_but').click()
    except Exception as e:
        print e
        driver.quit()
    else:
        next_page=driver.find_element_by_link_text(u'下一页')
        print driver.current_url
        while next_page:
            new_url=driver.current_url
            text=requests.get(new_url,headers=headers)
            et=etree.HTML(text.content)
            line=et.xpath("//div[@class='el']")
            for i in line:
                tx=etree.tostring(i,pretty_print=True)
                cont=HTMLParser.HTMLParser().unescape(tx)
                readtext(cont,path)
            driver.find_element_by_link_text(u'下一页').click()
            print driver.current_url
        driver.quit()
def readtext(cont,path):
    print cont
    a=b=c=d=e=f=''
    a=txt_wrap_by('html">','</',cont)
    b=txt_wrap_by('href="','" onmousedown',cont)
    c=txt_wrap_by('">','</',cont)
    d=txt_wrap_by('">','</',cont)
    e=txt_wrap_by('">','</',cont)
    f=txt_wrap_by('title="','" href',cont)
    list_data=[f,b,a,c,d,e]
    for i in list_data:
        print i
    write_xls(list_data,path)


def write_xls(list_data,path):
    wk=xlrd.open_workbook(path)
    sheet=wk.sheet_by_name('Sheet1')
    wb=copy(wk)
    for i in list_data:
        wb.get_sheet(0).write(sheet.nrows,list_data.index(i),i)
    wb.save(path)

def txt_wrap_by(start_str, end, html):
    start = html.find(start_str)
    if start >= 0:
        start += len(start_str)
        end = html.find(end, start)
        if end >= 0:
            return html[start:end].strip()
def  testexist(path):
    if not os.path.exists(path):
        w= xlwt.Workbook()
        w.add_sheet('Sheet1')
        w.save(path)
    else:
        os.remove(path)
        w= xlwt.Workbook()
        w.add_sheet('Sheet1')
        w.save(path)
if __name__=='__main__':
    path='E:\\0930\\ceshi.xls'
    testexist(path)
    #随意输入职位
    job=u'运维工程师'
    url_do(path,job)