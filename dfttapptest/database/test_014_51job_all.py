#coding:utf-8
import HTMLParser
from selenium import webdriver
import time,os,requests,xlwt,xlrd
from lxml import etree
from xlutils.copy import copy


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
            line=et.xpath("//div[@class='el']/span[@class and not(@id) and not(@onclick) and not(contains(@class,'title')) and not(contains(@class,'more dicon Dm'))]")
            for i in line:
                tx=etree.tostring(i,pretty_print=True)
                cont=HTMLParser.HTMLParser().unescape(tx)
                readtext(line.index(i),cont,path)
            driver.find_element_by_link_text(u'下一页').click()
            print driver.current_url
        driver.quit()
def readtext(index,cont,path):
    global a,b,c,d,e
    if index%4==0:
        a=txt_wrap_by('title="','" href',cont)
        b=txt_wrap_by('href="','">',cont)
    if index%4==1:
        c=txt_wrap_by('">','</',cont)
    if index%4==2:
        d=txt_wrap_by('">','</',cont)
    if index%4==3:
        e=txt_wrap_by('">','</',cont)
    if index!=0 and index%4==0:
        list_data=[a,b,c,d,e]
        write_xls(list_data,path)
        a=b=c=d=e=''

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
    path='E:\\0930\\java.xls'
    testexist(path)
    job=u'java开发工程师'
    url_do(path,job)