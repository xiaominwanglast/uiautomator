#coding:utf-8
import os
import time
import  unittest
import sys
from apptest.Public import readconfig


sys.path.append (r"..")
from appium import  webdriver
from apptest.Public  import write_represult
from apptest.Public  import processfile
from apptest.PO import  BasePage


class initunit(unittest.TestCase):

    error_excelpath="E:\\wxm\\pycharm\\python\\android_warning\\apptest\\result\\excel\\"
#    work_path=os.path.dirname(os.getcwd())+"\\screen\\nologin\search\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"\\"
    excelfile="ErrorReport.xls"

    passfile="PassReport.xls"

    time_excelpath="E:\\wxm\\pycharm\\python\\android_warning\\apptest\\result\\"
    timefile="case_spend_time.xls"


    def setUp(self):
        self.starttime=time.time()
#        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',BasePage.Base.capabilities)
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',BasePage.Base.capabilities)
        self.app=BasePage.Base.capabilities['appPackage']



    def tearDown(self):
        self.endtime=time.time()
        self.spendtime=int(self.endtime)-int(self.starttime)
        #计算结束的时间
        self.strtime1=time.strftime("%M:%S",time.localtime(self.spendtime))


        self.name1=self.__class__.__name__+'.'+self._testMethodName

        content=[self.name1,str(self.strtime1),"",""]
        #将结果写到excel中
        processfile.testdirexists(self.time_excelpath)

        write_represult.writefile(self.time_excelpath+self.timefile,content)

        #将出现error的情况写入到ErrorReport.xls文件中
        self.driver.quit()
        if self._resultForDoCleanups.errors:
            MethodName = self ._resultForDoCleanups.errors[-1][0]._testMethodName
            str1=str(self ._resultForDoCleanups.errors[-1][0])
            str2=str(self ._resultForDoCleanups.errors[-1][1])
#            print str1
            str1=str1.split('.')[-1]
            #组合得到出现error的类名
#            start=str1.find(".")
            end=str1.find(")")
#            ClassName=str1[start+1:end]
            ClassName=str1[:end]
            writestr=ClassName+'.'+MethodName
        #    content=[writestr,"Error"," "]
            content=[writestr,"Error",str2,' ']
            print content
            #将截图路径和运行的类名写入到excel中
            processfile.testdirexists(self.error_excelpath)
            write_represult.writefile(self.error_excelpath+self.excelfile,content)
            self._resultForDoCleanups.errors=[]
        else:
            content1=[self.name1,"Pass"," "," "]
            #将结果写到excel中
            processfile.testdirexists(self.error_excelpath)
            write_represult.writefile(self.error_excelpath+self.passfile,content1)
