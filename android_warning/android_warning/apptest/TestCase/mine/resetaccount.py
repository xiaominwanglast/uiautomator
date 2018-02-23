#coding:utf-8

from apptest.PO import Superunit
from apptest.PO import MinePage
from apptest.Public.getmethodname import GetName
from apptest.PO import BasePage
from apptest.Public.screenshot import screenshot
from apptest.Public.sendemail import smail
import os ,time
from apptest.PO import NewsPage
from apptest.PO import PursePage
from PIL import Image
from apptest.PO import LoginPage
from apptest.PO import SetPage
from random import  randint
from apptest.Public import processfile
#手机号另行登陆测试
class accountreset(Superunit.initunit):
    work_path=os.path.dirname(os.getcwd())+"\\screen\\mine\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"
    screen=os.path.dirname(os.getcwd())+"\\screen\\mine\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"
    def test_01_account(self):
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        MinePage.Mine(self.driver).click_mine_entry()
        LoginPage.Login(self.driver).input_nologin()
        try:
            self.assertTrue(LoginPage.Login(self.driver).find_getcode())
            LoginPage.Login(self.driver).click_quicklogin()
        except:
            pass
        LoginPage.Login(self.driver).input_username("13262860620")
        LoginPage.Login(self.driver).input_password("wang12345")
        LoginPage.Login(self.driver). click_submit()
        MinePage.Mine(self.driver).click_set()
        SetPage.Set(self.driver).click_tvaccount()
        try:
            self.assertTrue(SetPage.Set(self.driver).find_headimg())
            self.assertTrue(SetPage.Set(self.driver).find_account())
            self.assertTrue(SetPage.Set(self.driver).find_name())
            self.assertTrue(SetPage.Set(self.driver).find_sex())
            self.assertTrue(SetPage.Set(self.driver).find_phone())
            self.assertTrue(SetPage.Set(self.driver).find_rlQQ())
        except:
            print (u"账户设置>手机账号>修改账户信息-界面显示异常")
            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
            body=u"账户设置>手机账号>修改账户信息-界面显示异常"
            smail().send_errormsg(str(filename),body,self.work_path)
        else:
            i=randint(0,100)
            rename='beyond'+str(randint(0,100))
            print i,rename
            SetPage.Set(self.driver).input_editname(rename)
            if i%3==0:
                SetPage.Set(self.driver).click_boy()
                SetPage.Set(self.driver).click_btn()
                a=LoginPage.Login(self.driver).find_nologin()
                processfile.testdirexists(self.screen)
                self.driver.get_screenshot_as_file(self.screen+"screen.png")
                rgb=Image.open(self.work_path+"screen.png").getpixel((a.location['x']+a.size['width'] *1/8,a.location['y']+a.size['width'] *1/2))
                try:
                    self.assertEqual(rgb[0],146)
                    self.assertEqual((MinePage.Mine(self.driver).find_logintip()).text,rename)
                except:
                    print (u"账户设置>手机账号>修改账户信息>修改姓名与性别-界面显示异常")
                    filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                    body1=u"账户设置>手机账号>修改账户信息>修改姓名与性别-界面显示异常"
        #            smail().send_errormsg(str(filename),body1,self.work_path)
            elif i%3==1:
                SetPage.Set(self.driver).click_girl()
                SetPage.Set(self.driver).click_btn()
                a=LoginPage.Login(self.driver).find_nologin()
                processfile.testdirexists(self.screen)
                self.driver.get_screenshot_as_file(self.screen+"screen.png")
                rgb=Image.open(self.work_path+"screen.png").getpixel((a.location['x']+a.size['width'] *1/8,a.location['y']+a.size['width'] *1/2))
                try:
                    self.assertEqual(rgb[0],245)
                    self.assertEqual(rgb[1],180)
                    self.assertEqual((MinePage.Mine(self.driver).find_logintip()).text,rename)
                except:
                    print (u"账户设置>手机账号>修改账户信息>修改姓名与性别-界面显示异常")
                    filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                    body2=u"账户设置>手机账号>修改账户信息>修改姓名与性别-界面显示异常"
          #          smail().send_errormsg(str(filename),body2,self.work_path)
            else:
                SetPage.Set(self.driver).click_secret()
                SetPage.Set(self.driver).click_btn()
                a=LoginPage.Login(self.driver).find_nologin()
                processfile.testdirexists(self.screen)
                self.driver.get_screenshot_as_file(self.screen+"screen.png")
                rgb=Image.open(self.work_path+"screen.png").getpixel((a.location['x']+a.size['width'] *1/8,a.location['y']+a.size['width'] *1/2))
                try:
                    self.assertEqual(rgb[0],229)
                    self.assertEqual((MinePage.Mine(self.driver).find_logintip()).text,rename)
                except:
                    print (u"账户设置>手机账号>修改账户信息>修改姓名与性别-界面显示异常")
                    filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                    body3=u"账户设置>手机账号>修改账户信息>修改姓名与性别-界面显示异常"
          #          smail().send_errormsg(str(filename),body3,self.work_path)

    #前提条件 已经登陆上面的13262860620手机号，并且手机号未绑定过任何信息
    def test_02_banding(self):
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        MinePage.Mine(self.driver).click_mine_entry()
        try:
            self.assertNotEqual((MinePage.Mine(self.driver).find_logintip()).text,u"手机登录/注册")
        except:
            pass
        else:
            MinePage.Mine(self.driver).click_purse()
            ele2=PursePage.purse(self.driver).find_login_total_bonus()
            a_num=ele2
            print a_num
            self.driver.back()
            MinePage.Mine(self.driver).click_set()
            SetPage.Set(self.driver).click_tvaccount()
            SetPage.Set(self.driver).click_rlQQ()
            SetPage.Set(self.driver).click_right()
            self.driver.find_element_by_name('1727500963').click()
            time.sleep(5)
            try:
                self.assertTrue(SetPage.Set(self.driver).find_jiebang())
            except:
                print (u"账户设置>手机账号>绑定第三方账户-失败")
                filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                body=u"账户设置>手机账号>绑定第三方账户-失败"
                smail().send_errormsg(str(filename),body,self.work_path)
            else:
                self.driver.back()
                LoginPage.Login(self.driver).click_exit()
                LoginPage.Login(self.driver).click_loginqq()
                SetPage.Set(self.driver).click_right()
                self.driver.find_element_by_name('1727500963').click()
                time.sleep(5)
                try:
                    self.assertNotEqual((MinePage.Mine(self.driver).find_logintip()).text,u"手机登录/注册")
                except:
                    pass
                else:
                    MinePage.Mine(self.driver).click_purse()
                    ele4=PursePage.purse(self.driver).find_login_total_bonus()
                    b_num=ele4
                    print b_num
                    self.driver.back()
                    try:
                        print a_num,b_num
                        self.assertEqual(int(a_num),int(b_num))
                    except:
                        print (u"绑定社交账号>手机注册用户>绑定第三方账号>登陆第三方账号>信息显示一致-异常")
                        filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                        body=u"绑定社交账号>手机注册用户>绑定第三方账号>登陆第三方账号>信息显示一致-异常"
                        smail().send_errormsg(str(filename),body,self.work_path)
                    else:
                        MinePage.Mine(self.driver).click_set()
                        SetPage.Set(self.driver).click_tvaccount()
                        SetPage.Set(self.driver).click_jiebang()
                        SetPage.Set(self.driver).click_tvlogin()
                        self.driver.back()
                        LoginPage.Login(self.driver).click_exit()
                        LoginPage.Login(self.driver).click_loginqq()
                        SetPage.Set(self.driver).click_right()
                        self.driver.find_element_by_name('1727500963').click()
                        time.sleep(5)
                        try:
                            SetPage.Set(self.driver).click_tvcancel()
                        except:
                            pass
                        MinePage.Mine(self.driver).click_purse()
                        ele5=PursePage.purse(self.driver).find_login_total_bonus()
                        c_num=ele5
                        self.driver.back()
                        try:
                            self.assertNotEqual(int(b_num),int(c_num))
                        except:
                            print (u"绑定社交账号>手机注册用户>绑定第三方账号>登陆第三方账号>解绑登陆第三方账号>积分显示一致-异常")
                            filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                            body=u"绑定社交账号>手机注册用户>绑定第三方账号>登陆第三方账号>解绑登陆第三方账号>积分显示一致-异常"
                            smail().send_errormsg(str(filename),body,self.work_path)


    #前提条件QQ 1727500963已经登陆并且已经绑定，手机号已经解绑
    def test_03_outqq(self):
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        MinePage.Mine(self.driver).click_mine_entry()
        try:
            self.assertNotEqual((MinePage.Mine(self.driver).find_logintip()).text,u"手机登录/注册")
        except:
            pass
        else:
            NewsPage.News(self.driver).click_news_entry()
            NewsPage.News(self.driver).click_topic()
            self.driver.back()
            BasePage.Base(self.driver).do_swipe(self.driver,"up")
            NewsPage.News(self.driver).click_topic()
            self.driver.back()
            MinePage.Mine(self.driver).click_mine_entry()
            MinePage.Mine(self.driver).click_set()
            SetPage.Set(self.driver).click_tvaccount()
            SetPage.Set(self.driver).click_jiebang()
            try:
                SetPage.Set(self.driver).click_tvlogin()
            except:
                pass
            ele=SetPage.Set(self.driver).find_bangding()
            try:
                self.assertEqual(len(ele),4)
            except:
                print (u"账户设置>第三方账号登陆>解绑-失败")
                filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                body=(u"账户设置>第三方账号登陆>解绑-失败")
                smail().send_errormsg(str(filename),body,self.work_path)
            else:
                self.driver.back()
                LoginPage.Login(self.driver).click_exit()
                LoginPage.Login(self.driver).click_loginqq()
                SetPage.Set(self.driver).click_right()
                self.driver.find_element_by_name('1727500963').click()
                try:
                    SetPage.Set(self.driver).click_tvcancel()
                except:
                    pass
                MinePage.Mine(self.driver).click_purse()
                ele4=PursePage.purse(self.driver).find_login_total_bonus()
                try:
                    self.assertEqual(int(ele4),0)
                except:
                    print (u"账户设置>第三方账号登陆>解绑积分清0>再次登陆第三方账号>积分-显示异常")
                    filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                    body1=u"账户设置>第三方账号登陆>解绑积分清0>再次登陆第三方账号>积分-显示异常"
                    smail().send_errormsg(str(filename),body1,self.work_path)

       #解绑掉上面的QQ，为下次测试提供条件
    def test_04_jiebangqq(self):
        MinePage.Mine(self.driver).click_mine_entry()
        try:
            self.assertNotEqual((MinePage.Mine(self.driver).find_logintip()).text,u"手机登录/注册")
        except:
            pass
        else:
            MinePage.Mine(self.driver).click_set()
            SetPage.Set(self.driver).click_tvaccount()
            SetPage.Set(self.driver).click_jiebang()
            try:
                SetPage.Set(self.driver).click_tvlogin()
            except:
                pass
            self.driver.back()
            LoginPage.Login(self.driver).click_exit()

    def test_05_jiebang(self):
        name1=self.__class__.__name__+'.'+GetName.get_current_function_name()
        MinePage.Mine(self.driver).click_mine_entry()
        try:
            self.assertEqual((MinePage.Mine(self.driver).find_logintip()).text,u"手机登录/注册")
        except:
            pass
        else:
            self.driver.find_element_by_id("%s:id/tv_qq"%self.app).click()
            time.sleep(4)
            try:
                BasePage.Base(self.driver).tapxy(0.5,0.8,self.driver,6)
            except:
                print (u"点击不成功")
            else:
                MinePage.Mine(self.driver).click_set()
                SetPage.Set(self.driver).click_tvaccount()
                try:
                    self.assertTrue(SetPage.Set(self.driver).find_headimg())
                    self.assertTrue(SetPage.Set(self.driver).find_phone())
                    self.assertTrue(SetPage.Set(self.driver).find_rlQQ())
                except:
                    print (u"账户设置>第三方账号>解绑界面-显示异常")
                    filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                    body=u"账户设置>第三方账号>解绑界面-显示异常"
                    smail().send_errormsg(str(filename),body,self.work_path)
                else:
                    SetPage.Set(self.driver).click_jiebang()
                    try:
                        self.assertTrue(SetPage.Set(self.driver).find_tip())
                        SetPage.Set(self.driver).click_tvcancel()
                    except:
                        print (u"账户设置>第三方账号>解绑提示-显示异常")
                        filename=screenshot().screencap(self.work_path,self.driver,name=name1)
                        body1=u"账户设置>第三方账号>解绑提示-显示异常"
                        smail().send_errormsg(str(filename),body1,self.work_path)

                self.driver.back()
                LoginPage.Login(self.driver).click_exit()

