#coding:utf-8
# coding:utf-8
import time,unittest,os
from PreRandy.randyData import preConditionForTest
from Public.Super_Unittest import SuperUnit
from Public.PageLocate import elementLocate
from Public.ResolveHtml import getPath
from Public.ResolveHtml import getFinalMoney
from Public.ResolveHtml import getLoginStatus

class StoreActivityWeiHuo(SuperUnit):
    """商城活动,达豆,尾货商品以及组合活动"""

    def test_000(self):
        """数据准备"""
        #新建优惠券
        #preConditionForTest().TestMysqlCoupon()
        #新建红包
        #preConditionForTest().createNewRedGift()
        #取消客服所有订单
        preConditionForTest().cancleOrderFromSQL()
        print u'新建优惠券5元,新建红包10元,发放达豆数量1000，取消客服所有订单'

    def test_001(self):
        """尾货闪销活动(总价超过满折活动)"""
        #更改达豆数量
        preConditionForTest().UpdateTestUserDadou()
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath(self.store_username)
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.weihuoGoodId))
        for s in range(7):
            elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='total']/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='dadou_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='dadou_no']").findElementByXpath().text!='0':
            elementLocate(self.driver,".//*[@id='dadou_check']").clickElementByXpath()
        current_money=getFinalMoney(self.driver.page_source)
        print u"购物车，尾货商品上架60，活动价格30，7件"
        print self._testMethodName,current_money
        # TODO 需要加入金额断言
        if current_money != 210.0:
            self.screenShot(getPath(self._testMethodName))
        self.assertTrue(current_money == 210.0)
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        elementLocate(self.driver,".//div[2]/div[2]/div[3]/button[2]").clickElementByXpath()
        time.sleep(2)
        # 取消订单
        preConditionForTest().cancleOrder()
        self.driver.refresh()
        time.sleep(2)

    def test_002(self):
        """尾货闪销，达豆活动(总价超过满折活动)"""
        #更改达豆数量
        preConditionForTest().UpdateTestUserDadou()
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath(self.store_username)
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.weihuoGoodId))
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='total']/div[2]/button").clickElementByXpath()

        current_money=getFinalMoney(self.driver.page_source)
        print u"购物车，尾货商品上架60，活动价格30，3件"
        print self._testMethodName,current_money
        # TODO 需要加入金额断言
        if current_money != 85.5:
            self.screenShot(getPath(self._testMethodName))
        self.assertTrue(current_money == 85.5)
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        elementLocate(self.driver,".//div[2]/div[2]/div[3]/button[2]").clickElementByXpath()
        time.sleep(2)
        # 取消订单
        preConditionForTest().cancleOrder()
        self.driver.refresh()
        time.sleep(2)

if __name__=='__main__':
    unittest.main()