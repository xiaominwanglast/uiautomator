#coding:utf-8

import unittest


from apptest.TestCase.nologin_testSearch import nologin_serach

if __name__=="__main__":
    for i in range (1,2):
        testunit=unittest.TestSuite()
#        testunit.addTest( unittest.defaultTestLoader.loadTestsFromTestCase(nologin_news.test_02_nologin))
#        testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(AppTelLogin))
#        testunit.addTest(AppLoginTest("test_01_login_QQ"))
 #       testunit.addTest(Nologin("test_02_nologin"))
  #      testunit.addTest(nologin_channelselect("test_02_rightleft"))
 #       testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(nologin_addchannel))

        testunit.addTest(nologin_serach("test_01_search"))
  #      testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(nologin_channelselect))
#        testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(nologin_channelUI))
 #       testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(nologin_channeltoutiao))
        unittest.TextTestRunner(verbosity=2).run(testunit)
