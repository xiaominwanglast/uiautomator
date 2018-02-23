#coding:utf-8
import time
import random
import os
import sys
sys.path.append(r'..')


from apptest.PO import CollectPage
from apptest.PO import Superunit

from apptest.Public.getmethodname import GetName
from apptest.Public.screenshot import screenshot
from apptest.Public.sendemail import smail
from apptest.PO.BasePage import Base

class delcollect(Superunit.initunit):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\delcollect\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"

    def test_01_delone_news(self):
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        print name1
        CollectPage.Collect(self.driver).click_mine()
        CollectPage.Collect(self.driver).click_mine_collect()
        time.sleep(2)
        try:
            CollectPage.Collect(self.driver).click_tv_text()
            time.sleep(2)
            CollectPage.Collect(self.driver).click_edit()
            i=random.randint(0,len(CollectPage.Collect(self.driver).find_els_cbdel())-1)
            newsname1=CollectPage.Collect(self.driver).find_topics()[i].get_attribute("name")
            print newsname1
            #选择需要删除的内容，然后点击删除按钮
            CollectPage.Collect(self.driver).find_els_cbdel()[i].click()
            CollectPage.Collect(self.driver).click_btn_del()
            try:
                newsname2=CollectPage.Collect(self.driver).find_topics()[i].get_attribute("name")
            except:
                newsname2="  "
            if (newsname1==newsname2):
                filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                body=u"收藏界面-删除单个新闻未成功"
                smail().send_errormsg(str(filename),body,self.work_path)
            else:
                 print (u"删除单个新闻成功")
        except:
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body=u"收藏界面-删除单个新闻异常"
            smail().send_errormsg(str(filename),body,self.work_path)


    def test_02_delall_news(self):

        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        print name1
        CollectPage.Collect(self.driver).click_mine()
        CollectPage.Collect(self.driver).click_mine_collect()
        time.sleep(2)
        try:
            CollectPage.Collect(self.driver).click_tv_text()
            time.sleep(2)
            CollectPage.Collect(self.driver).click_edit()
            CollectPage.Collect(self.driver).click_select_all()
            CollectPage.Collect(self.driver).click_btn_del()
            try:
                self.assertFalse(CollectPage.Collect(self.driver).find_topics())
            except:
                filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                body=u"收藏界面-删除全部新闻未成功"
                smail().send_errormsg(str(filename),body,self.work_path)
        except:
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body=u"收藏界面-删除全部新闻异常"
            smail().send_errormsg(str(filename),body,self.work_path)




    def test_03_delone_pics (self):
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        print name1
        CollectPage.Collect(self.driver).click_mine()
        CollectPage.Collect(self.driver).click_mine_collect()
        time.sleep(2)
        try:
            CollectPage.Collect(self.driver).click_tv_image()
            time.sleep(2)
            CollectPage.Collect(self.driver).click_edit()
            newsname1=CollectPage.Collect(self.driver).find_topics()[0].get_attribute("name")
            print newsname1
            #选择需要删除的内容，然后点击删除按钮
            CollectPage.Collect(self.driver).find_els_cbdel()[0].click()
            CollectPage.Collect(self.driver).click_btn_del()
            try:
                newsname2=CollectPage.Collect(self.driver).find_topics()[0].get_attribute("name")
            except:
                newsname2="  "
            if (newsname1==newsname2):
                filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                body=u"收藏界面-删除单个图片未成功"
                smail().send_errormsg(str(filename),body,self.work_path)
            else:
                 print (u"删除单个图片成功")
        except:
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body=u"收藏界面-删除单个图片未异常"
            smail().send_errormsg(str(filename),body,self.work_path)



    def test_04_delall_pics(self):
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        print name1
        CollectPage.Collect(self.driver).click_add_channel()
        try:
            self.driver.find_element_by_name(u"美女").click()
        except:
            CollectPage.Collect(self.driver).click_channel_add()
            CollectPage.Collect(self.driver).click_channel_search()
            el=CollectPage.Collect(self.driver).click_search_edit()
            el.click()
            time.sleep(2)
            el.send_keys(u"美女")
            CollectPage.Collect(self.driver).click_btn_search()
            CollectPage.Collect(self.driver).click_btn_subscribe()
            for i in range (1,3):
                CollectPage.Collect(self.driver).click_back()
            self.driver.find_element_by_name(u"美女").click()
            time.sleep(2)
        for i in range (0,4):
            try:
                self.assertTrue(CollectPage.Collect(self.driver).find_favorite_image())
                CollectPage.Collect(self.driver).click_favorite_image()
            except:
                Base(self.driver).do_swipe(self.driver,"up")
            Base(self.driver).do_swipe(self.driver,"bigup")
        try:
            CollectPage.Collect(self.driver).click_mine()
        except:
            self.driver.back()
            CollectPage.Collect(self.driver).click_mine()
        CollectPage.Collect(self.driver).click_mine_collect()
        time.sleep(2)
        try:
            CollectPage.Collect(self.driver).click_tv_image()
            time.sleep(2)
            CollectPage.Collect(self.driver).click_edit()
            CollectPage.Collect(self.driver).click_select_all()
            CollectPage.Collect(self.driver).click_btn_del()
            try:
                self.assertFalse(CollectPage.Collect(self.driver).find_topics())
            except:
                filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                body=u"收藏界面-删除全部图片未成功"
                smail().send_errormsg(str(filename),body,self.work_path)
            else:
                 print (u"删除全部图片成功")
        except:
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body=u"收藏界面-删除全部图片异常"
            smail().send_errormsg(str(filename),body,self.work_path)
