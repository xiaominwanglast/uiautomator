#coding:utf-8
import unittest
import os,time
from Public import HTMLTestRunnerCN
from TestCase.storeActivityBase import StoreActivityBase
from TestCase.storeActivityZengDou import StoreActivityZengDou
from TestCase.storeActivityManJian import StoreActivityManJian
from TestCase.storeActivityManJianTD import StoreActivityManJianTD
from TestCase.storeActivityManZhe import StoreActivityManZhe
from TestCase.storeActivityManZeng import StoreActivityManZeng
from TestCase.storeActivityHeiKa import StoreActivityHeiKa
from TestCase.storeActivityWeiHuo import StoreActivityWeiHuo
from Public.readconfig import removeall
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def do_TestUnit():
    print u'--------------开始执行测试用例----------------'
    testSuit=unittest.TestSuite()
    testSuit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(StoreActivityBase))
    testSuit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(StoreActivityZengDou))
    testSuit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(StoreActivityManJian))
    testSuit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(StoreActivityManJianTD))
    testSuit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(StoreActivityManZhe))
    testSuit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(StoreActivityManZeng))
    testSuit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(StoreActivityHeiKa))
    testSuit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(StoreActivityWeiHuo))

    #清空截图
    screen_path = os.path.dirname(os.getcwd()) + '\\ScreenShot'
    result_path = os.path.dirname(os.getcwd()) + '\\TestResult'
    for path in [screen_path,result_path]:
        removeall(path)
    #定义个报告存放路径，支持相对路径
    now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
    print u'开始时间',now
    filename =os.path.dirname(os.getcwd())+ '\\TestResult\\'+now+"-result.html"
    fp = file(filename, 'wb')
    #定义测试报告
    runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp, title=u'店达商城自动化测试报告',description=u'详细测试报告:')
    #运行测试用例
    runner.run(testSuit)
    fp.close()
    end=time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
    print u'结束时间',end
if __name__=="__main__":
    do_TestUnit()
