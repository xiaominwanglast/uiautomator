#coding:utf-8
import requests
import unittest
import re
class interface(unittest.TestCase):
    def setUp(self):
        self.inter={}
        self.inter={'news':'http://refreshnews.dftoutiao.com/toutiao_appnew02/newspool',
                    'channel':'http://tjv1.dftoutiao.com/app/columns02',
                    'otherlogin':'http://user.dftoutiao.com/ucenter/otheruser/otherlogin',
                    'login':'http://user.dftoutiao.com/ucenter/otheruser/login',
                    'videos':'http://video.dftoutiao.com/app_video/getvideos'}
    def test(self):
        for value in self.inter.values():
            if (500 == requests.get(value).status_code or 200 == requests.get(value).status_code):
                print (u"网络正常")
            else:
                print (u"网络异常")
                print requests.get(value).status_code
if __name__=="__main__":
    unittest.main()