#coding:utf-8
from selenium import webdriver
import time
from xlutils.copy import copy
import xlwt,xlrd,os
import smtplib
from email.utils import formatdate
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys
def testfileexists(filepath):
    if not os.path.exists(filepath):
        w= xlwt.Workbook()
        w.add_sheet(u'Sheet1')
        w.save(filepath)
    else:
        os.remove(filepath)
        w= xlwt.Workbook()
        w.add_sheet(u'Sheet1')
        w.save(filepath)
def testdirexists(dirpath):
    if (not os.path.exists(dirpath)):
        os.makedirs(dirpath)
    else:
        pass
def getpagedata(page,driver):
    if page==u"首页":
        time.sleep(3)
        try:
            warmnewsup=driver.find_element_by_css_selector(".gg-pic-2.gg-pic-lp.fl").get_attribute("innerHTML").strip()
        except:
            try:
                driver.implicitly_wait(4)
                warmnewsup=driver.find_element_by_css_selector(".gg-pic-2.gg-pic-lp.fl").get_attribute("innerHTML").strip()
            except:
                time.sleep(3)
                warmnewsup=driver.page_source.encode('gb18030').strip()
        try:
            warmnewsdown=driver.find_element_by_css_selector(".gg-pic-2.gg-pic-rp.fl").get_attribute('innerHTML').strip()
        except:
            try:
                driver.implicitly_wait(4)
                warmnewsdown=driver.find_element_by_css_selector(".gg-pic-2.gg-pic-rp.fl").get_attribute('innerHTML').strip()
            except:
                time.sleep(1)
                warmnewsdown=driver.page_source.encode('gb18030').strip()
        try:
            readdown=driver.find_element_by_css_selector(".gg-index-2.mt10").get_attribute('innerHTML').strip()
        except:
            try:
                driver.implicitly_wait(4)
                readdown=driver.find_element_by_css_selector(".gg-index-2.mt10").get_attribute('innerHTML').strip()
            except:
                time.sleep(1)
                readdown=driver.page_source.encode('gb18030').strip()
        try:
            societydown=driver.find_element_by_css_selector(".gg-index-5.mt30").get_attribute('innerHTML').strip()
        except:
            try:
                driver.implicitly_wait(4)
                societydown=driver.find_element_by_css_selector(".gg-index-5.mt30").get_attribute('innerHTML').strip()
            except:
                societydown=driver.page_source.encode('gb18030').strip()
        try:
            militarydown=driver.find_element_by_css_selector(".gg-index-7.mt30").get_attribute('innerHTML').strip()
        except:
            try:
                driver.implicitly_wait(4)
                militarydown=driver.find_element_by_css_selector(".gg-index-7.mt30").get_attribute('innerHTML').strip()
            except:
                time.sleep(1)
                militarydown=driver.page_source.encode('gb18030').strip()
        try:
            fashiondown=driver.find_element_by_css_selector(".gg-index-8.mt30").get_attribute('innerHTML').strip()
        except:
            try:
                driver.implicitly_wait(4)
                fashiondown=driver.find_element_by_css_selector(".gg-index-8.mt30").get_attribute('innerHTML').strip()
            except:
                fashiondown=driver.page_source.encode('gb18030').strip()
        try:
            financedown=driver.find_element_by_css_selector(".gg-index-13.mt30").get_attribute('innerHTML').strip()
        except:
            try:
                driver.implicitly_wait(4)
                financedown=driver.find_element_by_css_selector(".gg-index-13.mt30").get_attribute('innerHTML').strip()
            except:
                time.sleep(1)
                financedown=driver.page_source.encode('gb18030').strip()
        try:
            sportsright=driver.find_element_by_css_selector(".gg-index-9.mt15").get_attribute('innerHTML').strip()
        except:
            try:
                driver.implicitly_wait(4)
                sportsright=driver.find_element_by_css_selector(".gg-index-9.mt15").get_attribute('innerHTML').strip()
            except:
                time.sleep(1)
                sportsright=driver.page_source.encode('gb18030').strip()
        try:
            scrollone=driver.find_element_by_css_selector(".section-bottom.gg-index-4.mt20").get_attribute('innerHTML').strip()
        except:
            try:
                driver.implicitly_wait(4)
                scrollone=driver.find_element_by_css_selector(".section-bottom.gg-index-4.mt20").get_attribute('innerHTML').strip()
            except:
                scrollone=driver.page_source.encode('gb18030').strip()
        try:
            scrolltwo=driver.find_element_by_css_selector(".section-bottom.gg-index-6.mt20").get_attribute('innerHTML').strip()
        except:
            try:
                driver.implicitly_wait(4)
                scrolltwo=driver.find_element_by_css_selector(".section-bottom.gg-index-6.mt20").get_attribute('innerHTML').strip()
            except:
                time.sleep(1)
                scrolltwo=driver.page_source.encode('gb18030').strip()
        try:
            scrollthree=driver.find_element_by_css_selector(".section-bottom.gg-index-11.mt20").get_attribute('innerHTML').strip()
        except:
            try:
                driver.implicitly_wait(4)
                scrollthree=driver.find_element_by_css_selector(".section-bottom.gg-index-11.mt20").get_attribute('innerHTML').strip()
            except:
                scrollthree=driver.page_source.encode('gb18030').strip()
        try:
            scrollfour=driver.find_element_by_css_selector(".section-bottom.gg-index-12.mt20").get_attribute('innerHTML').strip()
        except:
            try:
                driver.implicitly_wait(4)
                scrollfour=driver.find_element_by_css_selector(".section-bottom.gg-index-12.mt20").get_attribute('innerHTML').strip()
            except:
                time.sleep(1)
                scrollfour=driver.page_source.encode('gb18030').strip()
        try:
            time.sleep(1)
            Source=driver.page_source.encode('gb18030').strip()
        except:
            Source=0
        try:
            time.sleep(2)
            pagesource=driver.page_source.encode('gb18030').strip()
        except:
            pagesource=0
        return [warmnewsup,warmnewsdown,readdown,societydown,militarydown,fashiondown,financedown,sportsright,scrollone,scrolltwo,scrollthree,scrollfour,Source,pagesource]
    if page==u"详情页":
        time.sleep(2)
        try:
            roofcolumn=driver.find_element_by_css_selector(".ggTopsildercnt0").get_attribute('innerHTML').strip()
        except:
            try:
                driver.implicitly_wait(3)
                roofcolumn=driver.find_element_by_css_selector(".ggTopsildercnt0").get_attribute('innerHTML').strip()
            except:
                roofcolumn=0
        try:
            time.sleep(3)
            secondgo=driver.find_element_by_xpath("/html/body/div[9]").get_attribute('innerHTML').strip()
            if u"站长统计" in secondgo:
                time.sleep(3)
                secondgo=driver.page_source.encode('gb18030').strip()
            if 'top_left()'not in secondgo:
                time.sleep(3)
                secondgo=driver.page_source.encode('gb18030').strip()
        except:
            time.sleep(4)
            secondgo=driver.page_source.encode('gb18030').strip()
            if 'top_left()'not in secondgo:
                time.sleep(3)
                secondgo=driver.page_source.encode('gb18030').strip()
        try:
            titledown=driver.find_element_by_css_selector(".gg_detail_cnt.clearfix").get_attribute('innerHTML').strip()
        except:
            try:
                driver.implicitly_wait(3)
                titledown=driver.find_element_by_css_selector(".gg_detail_cnt.clearfix").get_attribute('innerHTML').strip()
            except:
                titledown=0
        try:
            bodydown=driver.find_element_by_css_selector(".gg_item_bomttom_cnt").get_attribute('innerHTML').strip()
        except:
            try:
                driver.implicitly_wait(3)
                bodydown=driver.find_element_by_css_selector(".gg_item_bomttom_cnt").get_attribute('innerHTML').strip()
            except:
                bodydown=0
        try:
            pagedown=driver.find_element_by_id("gg_item_bomttom_cnt-bk").get_attribute('innerHTML').strip()
        except:
            try:
                driver.implicitly_wait(3)
                pagedown=driver.find_element_by_id("gg_item_bomttom_cnt-bk").get_attribute('innerHTML').strip()
            except:
                pagedown=0
        try:
            nextdown=driver.find_element_by_css_selector(".ggPic_item_bomttom_cnt").get_attribute('innerHTML').strip()
        except:
            try:
                driver.implicitly_wait(3)
                nextdown=driver.find_element_by_css_selector(".ggPic_item_bomttom_cnt").get_attribute('innerHTML').strip()
            except:
                nextdown=0
        try:
            newsfocus=driver.find_element_by_css_selector(".guess_contain.guess_ad").get_attribute('innerHTML').strip()
        except:
            try:
                driver.implicitly_wait(3)
                newsfocus=driver.find_element_by_css_selector(".guess_contain.guess_ad").get_attribute('innerHTML').strip()
            except:
                newsfocus=0
        try:
            guesslike=driver.find_element_by_xpath(".//*[@class='bottom_over_cnt']/div[5]/div[@class='guess_contain']").get_attribute('innerHTML').strip()
        except:
            try:
                driver.implicitly_wait(3)
                guesslike=driver.find_element_by_xpath(".//*[@class='bottom_over_cnt']/div[5]/div[@class='guess_contain']").get_attribute('innerHTML').strip()
            except:
                guesslike=0
        try:
            hotdown=driver.find_element_by_css_selector(".guess_like.clear-fix.gg_bottom_cyup360").get_attribute('innerHTML').strip()
        except:
            try:
                driver.implicitly_wait(3)
                hotdown=driver.find_element_by_css_selector(".guess_like.clear-fix.gg_bottom_cyup360").get_attribute('innerHTML').strip()
            except:
                hotdown=0
        try:
            up360=driver.find_element_by_css_selector(".guess_like.gg_cyup360.clear-fix").get_attribute('innerHTML').strip()
        except:
            try:
                driver.implicitly_wait(3)
                up360=driver.find_element_by_css_selector(".guess_like.gg_cyup360.clear-fix").get_attribute('innerHTML').strip()
            except:
                up360=0
        try:
            newsrightone=driver.find_element_by_css_selector(".gg_channel_r_b.gg_channel_r_b_t.gg_right1").get_attribute('innerHTML').strip()
        except:
            try:
                driver.implicitly_wait(3)
                newsrightone=driver.find_element_by_css_selector(".gg_channel_r_b.gg_channel_r_b_t.gg_right1").get_attribute('innerHTML').strip()
            except:
                newsrightone=0
        try:
            newsrighttwo=driver.find_element_by_css_selector(".gg_channel_r_b.gg_detail_baidu.clear-fix.gg_right2").get_attribute('innerHTML').strip()
        except:
            try:
                driver.implicitly_wait(3)
                newsrighttwo=driver.find_element_by_css_selector(".gg_channel_r_b.gg_detail_baidu.clear-fix.gg_right2").get_attribute('innerHTML').strip()
            except:
                newsrighttwo=0
        try:
            newsrightthree=driver.find_element_by_css_selector(".gg_channel_r_b.gg_right3").get_attribute('innerHTML').strip()
        except:
            try:
                driver.implicitly_wait(3)
                newsrightthree=driver.find_element_by_css_selector(".gg_channel_r_b.gg_right3").get_attribute('innerHTML').strip()
            except:
                newsrightthree=0
        try:
            littlenews=driver.find_element_by_css_selector(".main_item_cnt.qiwenyishi").get_attribute('innerHTML').strip()
        except:
            try:
                driver.implicitly_wait(3)
                littlenews=driver.find_element_by_css_selector(".main_item_cnt.qiwenyishi").get_attribute('innerHTML').strip()
            except:
                littlenews=0
        try:
            rightfour=driver.find_element_by_css_selector(".gg_channel_r_b.gg_right4").get_attribute('innerHTML').strip()
        except:
            try:
                driver.implicitly_wait(3)
                rightfour=driver.find_element_by_css_selector(".gg_channel_r_b.gg_right4").get_attribute('innerHTML').strip()
            except:
                rightfour=0
        try:
            rightsix=driver.find_element_by_css_selector(".gg_channel_r_b.gg_right6").get_attribute('innerHTML').strip()
        except:
            try:
                driver.implicitly_wait(3)
                rightsix=driver.find_element_by_css_selector(".gg_channel_r_b.gg_right6").get_attribute('innerHTML').strip()
            except:
                rightsix=0
        try:
            rightseven=driver.find_element_by_css_selector(".gg_channel_r_b.gg_right7").get_attribute('innerHTML').strip()
        except:
            try:
                driver.implicitly_wait(3)
                rightseven=driver.find_element_by_css_selector(".gg_channel_r_b.gg_right7").get_attribute('innerHTML').strip()
            except:
                rightseven=0
        try:
            righteight=driver.find_element_by_css_selector(".gg_channel_r_b.gg_right8").get_attribute('innerHTML').strip()
        except:
            try:
                driver.implicitly_wait(3)
                righteight=driver.find_element_by_css_selector(".gg_channel_r_b.gg_right8").get_attribute('innerHTML').strip()
            except:
                righteight=0
        try:
            rightnine=driver.find_element_by_css_selector(".gg_channel_r_b.gg_right9").get_attribute('innerHTML').strip()
        except:
            try:
                driver.implicitly_wait(3)
                rightnine=driver.find_element_by_css_selector(".gg_channel_r_b.gg_right9").get_attribute('innerHTML').strip()
            except:
                rightnine=0
        searchsuggest=0
        try:
            picadd=driver.find_element_by_xpath("/html/body/script[11]").get_attribute('innerHTML').strip()
            if "tujia" in picadd:
                time.sleep(2)
                picadd=driver.find_element_by_xpath("/html/body/script[11]").get_attribute('innerHTML').strip()
            if "tujia" in picadd:
                picadd=driver.page_source.encode('gb18030').strip()
        except:
            try:
                driver.implicitly_wait(3)
                picadd=driver.page_source.encode('gb18030').strip()
            except:
                picadd=0
        leftdownSC=0
        try:
            time.sleep(3)
            ceSC=driver.page_source.encode('gb18030').strip()
        except:
            ceSC=0
        try:
            time.sleep(2)
            pagesource=driver.page_source.encode('gb18030').strip()
        except:
            pagesource=0
        return [roofcolumn,secondgo,titledown,bodydown,pagedown,nextdown,newsfocus,guesslike,hotdown,up360,newsrightone,newsrighttwo,newsrightthree,littlenews,rightfour,rightsix,rightseven,righteight,rightnine,searchsuggest,picadd,leftdownSC,ceSC,pagesource]
    if page==u"分页页面":
        time.sleep(3)
        try:
            roofright=driver.find_element_by_css_selector(".sy-top").get_attribute('innerHTML').strip()
        except:
            try:
                driver.implicitly_wait(3)
                roofright=driver.find_element_by_css_selector(".sy-top").get_attribute('innerHTML').strip()
            except:
                roofright=0
        try:
            pageone=driver.find_element_by_css_selector(".sy-1").get_attribute('innerHTML').strip()
        except:
            try:
                driver.implicitly_wait(3)
                pageone=driver.find_element_by_css_selector(".sy-1").get_attribute('innerHTML').strip()
            except:
                pageone=0
        try:
            pagetwo=driver.find_element_by_css_selector(".sy-2").get_attribute('innerHTML').strip()
        except:
            try:
                driver.implicitly_wait(3)
                pagetwo=driver.find_element_by_css_selector(".sy-2").get_attribute('innerHTML').strip()
            except:
                pagetwo=0
        try:
            pagethree=driver.find_element_by_css_selector(".sy-3").get_attribute('innerHTML').strip()
        except:
            try:
                driver.implicitly_wait(3)
                pagethree=driver.find_element_by_css_selector(".sy-3").get_attribute('innerHTML').strip()
            except:
                pagethree=0
        try:
            pagefour=driver.find_element_by_css_selector(".sy-4").get_attribute('innerHTML').strip()
        except:
            try:
                driver.implicitly_wait(5)
                pagefour=driver.find_element_by_css_selector(".sy-4").get_attribute('innerHTML').strip()
            except:
                pagefour=0
        try:
            time.sleep(2)
            pagesource=driver.page_source.encode('gb18030').strip()
        except:
            pagesource=0
        return [roofright,pageone,pagetwo,pagethree,pagefour,pagesource]
    if page==u"图片站":
        time.sleep(2)
        try:
            roofcolumn=driver.find_element_by_id("channel_top_1").get_attribute('innerHTML').strip()
        except:
            try:
                driver.implicitly_wait(3)
                roofcolumn=driver.find_element_by_id("channel_top_1").get_attribute('innerHTML').strip()
            except:
                roofcolumn=0
        try:
            nextpicup=driver.find_element_by_xpath('//*[@id="lastbdCnt"]/div[2]/div[2]').get_attribute('innerHTML').strip()
        except:
            try:
                driver.implicitly_wait(3)
                nextpicup=driver.find_element_by_xpath('//*[@id="lastbdCnt"]/div[2]/div[2]').get_attribute('innerHTML').strip()
            except:
                nextpicup=0
        try:
            nextpicdown=driver.find_element_by_xpath('//*[@id="lastbdCnt"]/div[2]/div[4]').get_attribute('innerHTML').strip()
        except:
            try:
                driver.implicitly_wait(3)
                nextpicdown=driver.find_element_by_xpath('//*[@id="lastbdCnt"]/div[2]/div[4]').get_attribute('innerHTML').strip()
            except:
                nextpicdown=0
        try:
            picdown=driver.find_element_by_css_selector('.picdowncntggcnt').get_attribute('innerHTML').strip()
        except:
            try:
                driver.implicitly_wait(3)
                picdown=driver.find_element_by_css_selector('.picdowncntggcnt').get_attribute('innerHTML').strip()
            except:
                picdown=0
        try:
            picsdown=driver.find_element_by_xpath(".//div[@class='tjContent']/div[1]").get_attribute('innerHTML').strip()
        except:
            try:
                driver.implicitly_wait(3)
                picsdown=driver.find_element_by_xpath(".//div[@class='tjContent']/div[1]").get_attribute('innerHTML').strip()
            except:
                picsdown=0
        try:
            guesslike=driver.find_element_by_xpath(".//div[@class='tjContent']/div[3]").get_attribute('innerHTML').strip()
        except:
            try:
                driver.implicitly_wait(5)
                guesslike=driver.find_element_by_xpath(".//div[@class='tjContent']/div[3]").get_attribute('innerHTML').strip()
            except:
                guesslike=0
        ceup=0
        leftdownup=0
        try:
            picadd=driver.find_element_by_xpath('/html/body/script[5]').get_attribute('innerHTML').strip()
        except:
            try:
                driver.implicitly_wait(5)
                picadd=driver.find_element_by_xpath('/html/body/script[5]').get_attribute('innerHTML').strip()
            except:
                picadd=0
        try:
            time.sleep(2)
            pagesource=driver.page_source.encode('gb18030').strip()
        except:
            pagesource=0
        return [roofcolumn,nextpicup,nextpicdown,picdown,picsdown,guesslike,ceup,leftdownup,picadd,pagesource]
    if page==u"频道页":
        time.sleep(2)
        try:
            roofcolumn=driver.find_element_by_css_selector('.header_cnt_2_detail').get_attribute('innerHTML').strip()
        except:
            try:
                driver.implicitly_wait(3)
                roofcolumn=driver.find_element_by_css_selector('.header_cnt_2_detail').get_attribute('innerHTML').strip()
            except:
                roofcolumn=0
        try:
            rightone=driver.find_element_by_css_selector('.gg_channel_r_b.gg_right1').get_attribute('innerHTML').strip()
        except:
            try:
                driver.implicitly_wait(3)
                rightone=driver.find_element_by_css_selector('.gg_channel_r_b.gg_right1').get_attribute('innerHTML').strip()
            except:
                rightone=0
        try:
            righttwo=driver.find_element_by_css_selector('.gg_channel_r_b.gg_right2').get_attribute('innerHTML').strip()
        except:
            try:
                driver.implicitly_wait(3)
                righttwo=driver.find_element_by_css_selector('.gg_channel_r_b.gg_right2').get_attribute('innerHTML').strip()
            except:
                righttwo=0
        try:
            rightthree=driver.find_element_by_css_selector('.gg_channel_r_b.gg_right3').get_attribute('innerHTML').strip()
        except:
            try:
                driver.implicitly_wait(3)
                rightthree=driver.find_element_by_css_selector('.gg_channel_r_b.gg_right3').get_attribute('innerHTML').strip()
            except:
                rightthree=0
        try:
            rightfour=driver.find_element_by_css_selector('.gg_channel_r_b.gg_right4').get_attribute('innerHTML').strip()
        except:
            try:
                driver.implicitly_wait(3)
                rightfour=driver.find_element_by_css_selector('.gg_channel_r_b.gg_right4').get_attribute('innerHTML').strip()
            except:
                rightfour=0
        try:
            rightfive=driver.find_element_by_css_selector('.gg_channel_r_b.gg_right5').get_attribute('innerHTML').strip()
        except:
            try:
                driver.implicitly_wait(5)
                rightfive=driver.find_element_by_css_selector('.gg_channel_r_b.gg_right5').get_attribute('innerHTML').strip()
            except:
                rightfive=0
        try:
            time.sleep(2)
            pagesource=driver.page_source.encode('gb18030').strip()
        except:
            pagesource=0
        return [roofcolumn,rightone,righttwo,rightthree,rightfour,rightfive,pagesource]

def datamain(page,j,cookie,key,sheetpage,pagedata,tempdata):
    sheetcols=sheetpage.ncols
    i=1
    temp=xlrd.open_workbook(tempdata)
    rows= temp.sheet_by_name("Sheet1").nrows
    wb=copy(temp)
    if cookie:
        for c in cookie:
            if c['name']=='MINI_QID_COOKIE':
                if c['value']==key:
                    for m in range(2,sheetcols):
                        if sheetpage.cell_value(j,m):
                            if type(sheetpage.cell_value(j,m))==float:
                                idvalue=str(int(sheetpage.cell_value(j,m)))
                            else:
                                idvalue=str(sheetpage.cell_value(j,m))
                            if pagedata[m-2]!=0:
                                try:
                                    if idvalue not in pagedata[m-2] and idvalue not in pagedata[len(pagedata)-1]:
                                        i=i+1
                                        wb.get_sheet(0).write(rows,0,page)
                                        wb.get_sheet(0).write(rows,1,key)
                                        wb.get_sheet(0).write(rows,i,u"%s-存在异常[%s]"%(sheetpage.cell_value(0,m),idvalue))
                                except:
                                    print u'数据格式异常或是数据异常'
                            else:
                                try:
                                    if idvalue not in pagedata[len(pagedata)-1]:
                                        i=i+1
                                        wb.get_sheet(0).write(rows,0,page)
                                        wb.get_sheet(0).write(rows,1,key)
                                        wb.get_sheet(0).write(rows,i,u"%s-存在异常[%s]"%(sheetpage.cell_value(0,m),idvalue))
                                except:
                                    print u'数据格式异常或是数据异常'
                    break
                else:
                    wb.get_sheet(0).write(rows,0,page)
                    wb.get_sheet(0).write(rows,1,key)
                    wb.get_sheet(0).write(rows,2,u"-qid(%s)与表格qid(%s)不同"%(c['value'],key))
                    break
    else:
        wb.get_sheet(0).write(rows,0,page)
        wb.get_sheet(0).write(rows,1,key)
        wb.get_sheet(0).write(rows,2,u"网络加载太慢或是网络异常未连接")
    wb.save(tempdata)

def urldata(page,listurl):
    url=''
    time=0
    if page==u"首页":
        time=32
        url=listurl[0]+'?'
    if page==u"详情页":
        time=35
        url=listurl[1]+'?'
    if page==u"分页页面":
        time=22
        url=listurl[2]+'?'
    if page==u"图片站":
        time=25
        url=listurl[3]+'?'
    if page==u"频道页":
        time=38
        url=listurl[4]+'?'
    return url,time

def sheetdata(listurl,sheetall):
    listname=[]
    for i in sheetall:
        listname.append(i.name)
    for i in sheetall:
        if i.name==u"首页" and listurl[0]=='':
            listname.remove(i.name)
        if i.name==u"详情页" and listurl[1]=='':
            listname.remove(i.name)
        if i.name==u"分页页面" and listurl[2]=='':
            listname.remove(i.name)
        if i.name==u"图片站" and listurl[3]=='':
            listname.remove(i.name)
        if i.name==u"频道页" and listurl[4]=='':
            listname.remove(i.name)
    return listname

def run(path,listurl):
    data=xlrd.open_workbook(path)
    sheetall=data.sheets()
    sheetalldata=sheetdata(listurl,sheetall)
    driver=''
    for m in sheetalldata:
        page=m
        sheetpage=data.sheet_by_name(page)
        onenrows=sheetpage.nrows
        for j in range(1,onenrows):
            if data.sheet_by_index(0).cell_value(j,1)=='':
                continue
            options = webdriver.ChromeOptions()
            options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
            urlall=urldata(page,listurl)
            url=urlall[0]
            if type(data.sheet_by_index(0).cell_value(j,1))==float:
                key=str(int(data.sheet_by_index(0).cell_value(j,1)))
            else:
                key=data.sheet_by_index(0).cell_value(j,1)
            print url+key
            try:
                driver = webdriver.Chrome(chrome_options=options)
                driver.set_page_load_timeout(urlall[1])
                driver.get(url+key)
                driver.maximize_window()
                pagedata=getpagedata(page,driver)
                len(driver.page_source.encode('gb18030'))
            except:
                driver.quit()
                for i in range(2):
                    driver = webdriver.Chrome(chrome_options=options)
                    driver.set_page_load_timeout(urlall[1])
                    try:
                        driver.get(url+key)
                        driver.maximize_window()
                        pagedata=getpagedata(page,driver)
                        len(driver.page_source.encode('gb18030'))
                    except:
                        print (u"网络加载出现异常")
                        if i==1:
                            cookie=[]
                            pagedata=[]
                            datamain(page,j,cookie,key,sheetpage,pagedata,tempdata)
                        driver.quit()
                        time.sleep(1)
                    else:
                        cookie=driver.get_cookies()
                        datamain(page,j,cookie,key,sheetpage,pagedata,tempdata)
                        driver.quit()
                        time.sleep(1)
                        break
            else:
                cookie=driver.get_cookies()
                datamain(page,j,cookie,key,sheetpage,pagedata,tempdata)
                driver.quit()
                time.sleep(1)

def urlpathdata(urlpath):
    urlfirstpage,urldetailspage,urlotherpage,urlpicpage,urlchannelpage=0,0,0,0,0
    src=xlrd.open_workbook(urlpath)
    rows=src.sheet_by_name('Sheet1').nrows
    for i in range(rows):
        if src.sheet_by_name('Sheet1').cell_value(i,0)==u'首页':
            urlfirstpage=src.sheet_by_name('Sheet1').cell_value(i,1).strip()
        if src.sheet_by_name('Sheet1').cell_value(i,0)==u'详情页':
            urldetailspage=src.sheet_by_name('Sheet1').cell_value(i,1).strip()
        if src.sheet_by_name('Sheet1').cell_value(i,0)==u'分页页面':
            urlotherpage=src.sheet_by_name('Sheet1').cell_value(i,1).strip()
        if src.sheet_by_name('Sheet1').cell_value(i,0)==u'图片站':
            urlpicpage=src.sheet_by_name('Sheet1').cell_value(i,1).strip()
        if src.sheet_by_name('Sheet1').cell_value(i,0)==u'频道页':
            urlchannelpage=src.sheet_by_name('Sheet1').cell_value(i,1).strip()
    listurl=[urlfirstpage,urldetailspage,urlotherpage,urlpicpage,urlchannelpage]
    return listurl
def readeconfig(emailpath):
    emaillist=[]
    src=xlrd.open_workbook(emailpath)
    rows=src.sheet_by_name('Sheet1').nrows
    for i in range(rows):
        emaillist.append(src.sheet_by_name('Sheet1').cell_value(i,2))
    return emaillist
def setuireport(filepath,emailpath):
    config=readeconfig(emailpath)
    msg = MIMEMultipart()
    subject=u'头条站web自动化测试报告_%s'%time.strftime('%Y%m%d',time.localtime(time.time()))
    smtpHost='smtp.exmail.qq.com'
    smtpPort =25
    sslPort  = 465

    fromMail = config[0]
    toMail=config[1].split(',')
    cc=config[2].split(',')

#发邮件的用户名和密码
    username = config[3]
    password = config[4]
#解决中文问题
    reload(sys)
#初始化邮件
    encoding = 'utf-8'
    msg['Subject'] = Header(subject,encoding)
    msg['From'] = fromMail
    msg['To'] = ','.join(toMail)
    msg['Date'] = formatdate()
    msg['Cc'] =','.join(cc)
#附加附件
    att3 = MIMEText(open(filepath, 'rb').read(), 'base64', 'gb2312')
    att3["Content-Type"] = 'application/octet-stream'
    att3["Content-Disposition"] = 'attachment; filename="toutiaozhan_testdata.xls"'#这里的filename可以任意写，写什么名字，邮件中显示什么名字
    msg.attach(att3)
    try:
        smtp = smtplib.SMTP_SSL(smtpHost,sslPort)
        smtp.ehlo()
        smtp.login(username,password)
    #发送邮件
        toaddress=toMail+cc
        smtp.sendmail(fromMail,toaddress,msg.as_string())
        smtp.close()
        print 'OK'
    except Exception as e:
        print e
        print 'Error: unable to send email'


file=u'E:\\mac\\id'
path=file+'\\'+u'头条已上传后台ID表 - 20170223.xls'
tempdata=file+'\\'+u'data.xls'
urlpath=file+'\\'+u'url.xls'
emailpath=file+'\\'+u'send_email.xls'
print u"web自动化打包版本V20170208.5".encode('gb18030')
print "-------------------------------------------"
print u"***确保工作目录e:\\mac\\id存在".encode('gb18030')
print u"***确保测试时不要打开data.xls数据表".encode('gb18030')
print u"***确保email表邮件配置正确，cc抄送不能为空并且分隔符逗号为英文形式".encode('gb18030')
print u"***确保工作目录下有测试网站url表、头条站广告位表、生成数据表、email表(表名分别为url.xls,data.xls,头条已上传后台ID表 - 20170223，send_email.xls)".encode('gb18030')
print "-------------------------------------------"
time.sleep(2)
print "-------------------------------------------"
print u"1.新增自动化测试结束自动发送邮件功能".encode('gb18030')
print u"2.新增第二次源码抓取复测".encode('gb18030')
print "-------------------------------------------"

listurl=urlpathdata(urlpath)
time.sleep(2)
testdirexists(file)
testfileexists(tempdata)
run(path,listurl)
setuireport(tempdata,emailpath)


