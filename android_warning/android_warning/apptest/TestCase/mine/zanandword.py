#coding:utf-8


from apptest.PO import Superunit
from apptest.PO import MinePage
from apptest.Public.getmethodname import GetName
from apptest.PO import NewsPage
from apptest.PO import BasePage
from apptest.PO import InsideNewsPage
from apptest.Public.screenshot import screenshot
from apptest.Public.sendemail import smail
import os ,time
from apptest.PO import LoginPage
from apptest.PO import TaskCenterPage
from apptest.PO import PursePage
from apptest.PO import InsideNewsPage
class zanANDword(Superunit.initunit):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\mine\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"

    def test_01_zanword(self):
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        times=[]
        MinePage.Mine(self.driver).click_mine_entry()
        LoginPage.Login(self.driver).input_nologin()
        try:
            self.assertTrue(MinePage.Mine(self.driver).find_logintip())
            self.assertTrue(LoginPage.Login(self.driver).find_tvcommand())
            self.assertTrue(LoginPage.Login(self.driver).find_tvtitle())
            self.assertTrue(LoginPage.Login(self.driver).find_tvtime())
        except:
            print (u"个人中心>点赞和评论-界面显示异常")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body=u"个人中心>点赞和评论-界面显示异常"
            smail().send_errormsg(str(filename),body,self.work_path)
        else:
            BasePage.Base(self.driver).do_swipe(self.driver,"up")
            for i in LoginPage.Login(self.driver).find_tvtime():
                b=time.mktime(time.strptime("2016-"+i.text+":00",'%Y-%m-%d %H:%M:%S'))
                times.append(int(b))
            if times[2]:
                if times[0]>=times[1]>=times[2]:
                    pass
                else:
                    print (u"个人中心>点赞和评论-时间顺序显示异常")
                    filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                    body1=u"个人中心>点赞和评论-时间顺序显示异常"
                    smail().send_errormsg(str(filename),body1,self.work_path)
            LoginPage.Login(self.driver).click_tvtile()
            try:
                self.assertTrue(InsideNewsPage.Inside(self.driver).find_configloc())
                self.assertFalse(LoginPage.Login(self.driver).find_tvcommand())
            except:
                print (u"个人中心>点赞和评论-跳转到内页显示异常")
                filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                body2=u"个人中心>点赞和评论-跳转到内页显示异常"
                smail().send_errormsg(str(filename),body2,self.work_path)
            else:
                self.driver.back()
                LoginPage.Login(self.driver).click_praise()
                try:
                    self.assertTrue(LoginPage.Login(self.driver).find_praisenum())
                except:
                    print (u"个人中心>点赞和评论-跳转到内页显示异常")
                    filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                    body3=u"个人中心>点赞和评论-跳转到内页显示异常"
                    smail().send_errormsg(str(filename),body3,self.work_path)
