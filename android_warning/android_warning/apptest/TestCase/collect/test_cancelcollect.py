#coding:utf-8
import time
import random
import os
import sys
sys.path.append(r'..')


from apptest.PO import CollectPage
from apptest.PO import Superunit
from apptest.PO import NewsPage
from apptest.Public.getmethodname import GetName
from apptest.Public.screenshot import screenshot
from apptest.Public.sendemail import smail

class cancel(Superunit.initunit):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\cancelcollect\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"
    def test_01_cancelnews(self):

        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        CollectPage.Collect(self.driver).click_mine()
        CollectPage.Collect(self.driver).click_mine_collect()
        time.sleep(2)
        try:
            CollectPage.Collect(self.driver).click_tv_text()
            time.sleep(2)
            self.assertTrue(CollectPage.Collect(self.driver).find_topics())
        except:
            pass
        else:
            #取一个随机数
            i=random.randint(0,len(CollectPage.Collect(self.driver).find_topics())-1)
            time.sleep(2)
            print i
            newsname1=CollectPage.Collect(self.driver).find_topics()[i].get_attribute("name")
            print newsname1
            CollectPage.Collect(self.driver).find_topics()[i].click()
            #点击取消收藏按钮
            CollectPage.Collect(self.driver).click_save_page()
            time.sleep(2)
            self.driver.back()
            try:
                newsname2=CollectPage.Collect(self.driver).find_topics()[i].get_attribute("name")
            except:
                newsname2 = " "
            if (newsname1==newsname2):
                print (u"收藏界面-取消新闻未成功")
                filename=screenshot().screencap(self.work_path,self.driver,name=name1)

                body=u"收藏界面-取消新闻未成功"
                smail().send_errormsg(str(filename),body,self.work_path)
            else:
                print  (u"取消收藏成功")


    def test_02_cancelvideos(self):

        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        CollectPage.Collect(self.driver).click_mine()
        CollectPage.Collect(self.driver).click_mine_collect()
        time.sleep(2)
        try:
            print (u"首次进行判断操作")
            CollectPage.Collect(self.driver).click_tv_video()
            time.sleep(2)
            self.assertTrue(CollectPage.Collect(self.driver).find_topics())
        except:
            pass
        else:
            i=random.randint(0,len(CollectPage.Collect(self.driver).find_topics())-1)
            time.sleep(2)
            sname=CollectPage.Collect(self.driver).find_titles_video()[i].get_attribute("name")
            CollectPage.Collect(self.driver).find_els_videossave()[i].click()
            time.sleep(2)
            self.driver.back()
            CollectPage.Collect(self.driver).click_mine_collect()
            time.sleep(2)
            CollectPage.Collect(self.driver).click_tv_video()
            time.sleep(2)
            try:
                tname=CollectPage.Collect(self.driver).find_titles_video()[i].get_attribute("name")
            except:
                tname=" "
            if (sname==tname):
                print (u"收藏界面-取消视频未成功")
                filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                body=u"收藏界面-取消视频未成功"
                smail().send_errormsg(str(filename),body,self.work_path)
            else:
                print (u"取消视频未成功")
