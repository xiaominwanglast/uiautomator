#coding:utf-8
import time
import requests
import redis
import json
import logging
import os
import urllib2
import hashlib
import MySQLdb
from warnings import filterwarnings
filterwarnings('ignore', category = MySQLdb.Warning)
class preConditionForTest(object):
    """
    测试环境，南京账号数据准备测试：
    1.发放优惠券, 满30减5
    2.发放红包，满40减10
    3.发放达豆，默认2000
    4.上架物品, 价格50,数量100
    5.本地存储用户名，logindevice表
    6.本地存储上架物品，productcz表
    7.本地存储优惠码，coupon表
    8.清除购物车redis缓存信息
    """
    def __init__(self):
        self.headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
                      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'}
        """
        server_url:测试环境后台url     
        url_username:后台登陆账号
        url_password:后台登陆密码
        """
        self.server_url = 'http://192.168.1.251:31010'
        self.url_username= '12345678910'
        self.url_password='123456'
        """
        test_db_ip:测试环境ip，默认端口3306
        test_user:用户名
        test_passwd:密码
        test_mainDb:测试环境 数据库
        """
        self.test_db_ip = '192.168.1.101'
        self.test_user = 'dddev'
        self.test_passwd = '123456'
        self.test_mainDb='ctcdb_new_test'
        """
        redis_db_ip:缓存数据库redis地址
        redis_port:redis端口
        redis_db:数据库0
        """
        self.redis_db_ip='192.168.1.101'
        self.redis_port=6379
        self.redis_db=0
        """
        service_url:客服系统地址
        service_username:客服登陆账号
        service_password:客服登陆密码
        """
        self.service_url='http://192.168.1.251:3586'
        self.service_username='12345678910'
        self.service_password='123456'
        """
        redGift_value:红包金额
        redGift_quantity:红包发放数量
        redGift_ownLimit:红包拥有限制量
        redGift_useBaseLine:红包使用条件
        redGift_instruction:描述
        """
        self.redGift_value=10
        self.redGift_quantity=5
        self.redGift_ownLimit=5
        self.redGift_useBaseLine=40
        self.redGift_instruction=u'满40减10'
        """
        coupon_value:优惠券金额
        coupon_quantity:优惠券发放数量
        coupon_useBaseLine:使用金额条件
        coupon_instruction:描述
        """
        self.coupon_value=5
        self.coupon_quantity=5
        self.coupon_useBaseLine=30
        self.coupon_instruction=u'满30减5'
        """
        session:初始化session节点
        """
        self.session=requests.Session()
        """
        conn_test:初始化链接测试环境数据库
        """
        self.conn_test = MySQLdb.connect(host=self.test_db_ip, user=self.test_user, passwd=self.test_passwd, port=3306,charset="utf8")
        """
        初始化log格式
        """
        # logging.basicConfig(
        #                     level=logging.DEBUG,
        #                     format='[%(asctime)s] [%(levelname)s] %(message)s',
        #                     datefmt='%Y_%m_%d %H:%M:%S',
        # )

        """
        store_url:商城地址
        store_main_username:主仓店铺账号13262860621
        store_main_password:主仓店铺密码
        store_Id:主仓店铺Id 161733
        cityId:连云港城市码
        dadouCount:发放达豆数量
        """
        self.store_url='http://192.168.1.251:30011'

    @property
    def store_main_username(self):
        return self.load_json()['storePhoneNum']

    @property
    def store_main_password(self):
        return self.load_json()['storePwd']

    @property
    def store_Id(self):
        return self.load_json()['storeId']

    @property
    def cityId(self):
        return self.load_json()['cityId']

    @property
    def dadouCount(self):
        return self.load_json()['dadou']

    @classmethod
    def load_json(cls,jsonfile=None):
        with open(os.path.dirname(os.getcwd()) + '\\Settings\\storeInfo.json', 'r') as load_f:
            load_json = json.load(load_f)
        return load_json

    @classmethod
    def changeIntoStr(cls,data,str_data=''):
        if isinstance(data, unicode):
            str_data = data.encode('utf-8')
        elif isinstance(data, str):
            str_data = data
        return str_data

    @classmethod
    def createOrderTime(cls):
        return time.strftime('%Y-%m-%d', time.localtime(time.time()))

    @classmethod
    def returnMd5(cls,pwd):
        md = hashlib.md5()
        md.update(pwd)
        return md.hexdigest()

    @staticmethod
    def createCouponTime():
        """
        南京的税换开始时间>可用开始时间
        :return: 返回发放开始时间，发放结束时间，可使用开始时间，可使用结束时间
        """
        grantStart = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()-24*60*60))
        useStart = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        useEnd = time.strftime('%Y-%m-%d', time.localtime(time.time() + 24 * 60 * 60))
        grantEnd = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() + 24 * 60 * 60))
        return grantStart, grantEnd, useStart, useEnd

    @staticmethod
    def createTime():
        """
        :return: 返回发放开始时间，发放结束时间，可使用开始时间，可使用结束时间
        """
        grantStart = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()- 1* 60 * 60))
        useStart = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()- 2* 60 * 60))
        useEnd = grantEnd = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() + 24 * 60 * 60))
        return grantStart, grantEnd, useStart, useEnd

    @staticmethod
    def createDayTime():
        """
        :return: 返回当前年月日，+1天年月日
        """
        StartDay = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        EndDay =   time.strftime('%Y-%m-%d', time.localtime(time.time() + 24 * 60 * 60))
        return StartDay,EndDay


    @staticmethod
    def createName():
        """
        :return:返回自动创建名字
        """
        couponName = u'自动测' + str(int(time.time()))
        return couponName

    def newCoupon(self):
        """
        创建优惠码
        :return:
        """
        couponName=self.createName()
        grantStart,grantEnd,useStart,useEnd=self.createCouponTime()
        #登陆后台
        login_url='{0}/users/login'.format(self.server_url)
        login_data={'userName':self.url_username,'password':self.url_password}
        login_response=self.session.post(url=login_url,data=login_data,headers=self.headers)
        #选择城市
        changzhou_url='{0}/users/updateAgency'.format(self.server_url)
        changzhou_data={'cityId':self.cityId,'agencyId':171}
        chanzhou_response=self.session.post(url=changzhou_url,data=changzhou_data,headers=self.headers)
        #创建单
        youhuiquan_url='{0}/json/management/coupon/addCoupon'.format(self.server_url)
        """
        type：2, 优惠码
        grantType:-1 无兑换条件
        lifeTime:-1 无领取时间限制
        """
        youhuiquan_data={'couponName':couponName,'type':2,'grantType':'-1','value':self.coupon_value,'grantStart':grantStart,
                         'grantEnd':grantEnd,'useStart':useStart,'useEnd':useEnd,
                         'lifeTime':'-1','quantity':self.coupon_quantity,'useBaseLine':self.coupon_useBaseLine,'instruction':self.coupon_instruction}
        youhuiquan_response=self.session.post(youhuiquan_url,data=youhuiquan_data,headers=self.headers)
        youhuiquan_strdata = self.changeIntoStr(youhuiquan_response.text)
        youhuiquan_json=json.loads(youhuiquan_strdata)
        #点击导出
        daochu_url='{0}/json/management/coupon/queryCoupon?id={1}'.format(self.server_url,str(youhuiquan_json['gift']['id']))
        daochu_response=self.session.get(url=daochu_url,headers=self.headers)
        daochu_data=self.changeIntoStr(daochu_response.text)
        testdata=json.loads(daochu_data)
        #拼接下载url地址
        test_url = '{7}/json/management/coupon/code/generate?couponCodeBaseSettingId={0}' \
            '&name={1}&useStart={2}&useEnd={3}&quantity={4}&value={5}&useBaseLine={6}'.format(  testdata['data']['id'],
                                                                                                urllib2.quote(testdata['data']['couponName'].encode('utf-8')),
                                                                                                testdata['data']['useStartTime'],
                                                                                                testdata['data']['useEndTime'],
                                                                                                testdata['data']['grantCount'],
                                                                                                testdata['data']['value'],
                                                                                                testdata['data']['useBaseLine'],
                                                                                                self.server_url)
        self.session.get(url=test_url,headers=self.headers)
        return youhuiquan_json['gift']['id'],youhuiquan_data['couponName']

    def TestMysqlCoupon(self):
        """
        链接测试环境数据库
        :returns:返回优惠码信息,giftID,couponName
        """
        giftID,couponName=self.newCoupon()
        cur = self.conn_test.cursor()
        self.conn_test.select_db(self.test_mainDb)
        count = cur.execute('select code from coupon_codes WHERE CouponCodeBaseSettingId = {0}'.format(giftID))
        info = cur.fetchmany(count)
        self.conn_test.commit()
        cur.close()
        for coupon in info:
            self.bindingCoupon(coupon[0])

    def bindingCoupon(self,couponCode):
        """
        绑定优惠券
        :return:
        """
        #登陆
        newSession=requests.Session()
        login_url='{0}/login'.format(self.store_url)
        login_reponse=newSession.post(url=login_url,data={'uid':self.store_main_username,'pwd':self.store_main_password,'auto':'true',
                                                            'plugin[sw]': 1920,'plugin[sh]': 1080,'plugin[iw]': 1916,'plugin[ih]': 264,
                                                            'plugin[ua]': self.headers},headers=self.headers)
        print login_reponse.text
        #绑定
        banding_url='{0}/api/user/assets/code/new'.format(self.store_url)
        banding_response=newSession.post(url=banding_url,data={'code':couponCode})
        print banding_response.text
    def clean_redis(self):
        """
        清空缓存购物车信息
        """
        rd = redis.Redis(host=self.redis_db_ip, port=self.redis_port, db=self.redis_db)
        key_ = 'cart:{0}'.format(self.store_Id)
        if rd.exists(key_):
            rd.delete(key_)
    def UpdateTestUserDadou(self):
        """
        更新账号达豆数量,默认改为2000
        """
        cur = self.conn_test.cursor()
        self.conn_test.select_db(self.test_mainDb)
        cur.execute("update stores set dadou={0} where id = {1}".format(self.dadouCount, self.store_Id))
        self.conn_test.commit()
        cur.execute("select dadou from stores where id = {0}".format(self.store_Id))
        print cur.fetchone()
        cur.close()

    def createNewRedGift(self):
        """
        创建红包
        :return:
        """
        name = self.createName()
        grantStart, grantEnd, useStart, useEnd = self.createTime()
        #登录
        login_url = '{0}/users/login'.format(self.server_url)
        login_data = {'userName':self.url_username,'password':self.url_password}
        login_response = self.session.post(url=login_url, data=login_data, headers=self.headers)
        #切换城市
        changzhou_url = '{0}/users/updateAgency'.format(self.server_url)
        changzhou_data = {'cityId': self.cityId, 'agencyId': 171}
        chanzhou_response = self.session.post(url=changzhou_url, data=changzhou_data, headers=self.headers)
        #新增红包
        redgift_url = '{0}/json/management/promotional/coupon/redgift/add'.format(self.server_url)
        """
        ownLimit:用户拥有限制数量
        vipRank:vip无限制
        lifeTime:使用周期不限制
        """
        redgift_data = {'name': name, 'type': u'普通红包', 'value': self.redGift_value, 'grantStart': grantStart,
                        'grantEnd': grantEnd, 'useStart': useStart, 'useEnd': useEnd,'lifeTime':-1,
                        'quantity': self.redGift_quantity, 'ownLimit': self.redGift_ownLimit, 'useBaseLine': self.redGift_useBaseLine,
                        'vipRank': '-1','instruction': self.redGift_instruction}
        redgift_response = self.session.post(redgift_url, data=redgift_data, headers=self.headers)
        redgift_str=self.changeIntoStr(redgift_response.text)
        redgift_json = json.loads(redgift_str)
        # logging.info(str(redgift_json))
        self.receiveRedGift()
        return redgift_json

    def receiveRedGift(self):
        """
        领取红包
        :return:
        """
        #登陆
        newSession=requests.Session()
        login_url='{0}/login'.format(self.store_url)
        login_reponse=newSession.post(url=login_url,data={'uid':self.store_main_username,'pwd':self.store_main_password,'auto':'true',
                                                            'plugin[sw]': 1920,'plugin[sh]': 1080,'plugin[iw]': 1916,'plugin[ih]': 264,
                                                            'plugin[ua]': self.headers},headers=self.headers)
        print login_reponse.text
        #领取
        giftUnUsed_url='{0}/api/user/assets/canUseCash'.format(self.store_url)
        giftUnUsed_response=newSession.post(url=giftUnUsed_url,data={"type":"money","offset":0,"limit":12})
        giftUnUsed_str=self.changeIntoStr(giftUnUsed_response.text)
        giftUnUsed_json=json.loads(giftUnUsed_str)
        for eveId in giftUnUsed_json['data']:
            id_=eveId['id']
            receive_url='{0}/api/home/first/redGift'.format(self.store_url)
            receive_response=newSession.post(url=receive_url,data={"redGiftId":id_})
            print receive_response.text

    def cancleOrder(self):
        start,end=self.createDayTime()
        #登陆客服
        newSession = requests.Session()
        service_login='{0}/service/api/manager/login'.format(self.service_url)
        service_response=newSession.post(url=service_login,data={'account':self.service_username,'password':self.service_password})
        print service_response.text
        #切换城市
        service_changecity_url='{0}/service/api/manager/updateAgency'.format(self.service_url)
        service_changecity_response=newSession.post(url=service_changecity_url,data={'cityId':320700,'agencyId':171})
        print service_changecity_response.text
        #查看当前订单
        check_url='{0}/service/api/order/list?offset=0&limit=1000&payType=1&order=store&start={1}%2000:00:00&end={2}%2000:00:00&message=0&timeTag=0'.format(self.service_url,start,end)
        check_url_response=newSession.get(url=check_url)
        check_json=json.loads(self.changeIntoStr(check_url_response.text))
        try:
            for cj in check_json['stores'][0]['orders']:
                if cj['state']==0:
                    #取消订单
                    cancle_url='{0}/service/api/order/cancel'.format(self.service_url)
                    cancle_response=newSession.post(url=cancle_url,data={'id':int(cj['id']),'info':u'客户下错单'})
                    # print cj['id'],cancle_response.text
        except Exception as e:
            print e
    def cancleOrderFromSQL(self):
        cur = self.conn_test.cursor()
        self.conn_test.select_db(self.test_mainDb)
        cur.execute("update store_goods_orders set state='-100' where CityId={0} and createdAt LIKE '%{1}%'".format(self.cityId,self.createOrderTime()))
        self.conn_test.commit()
        cur.close()

if __name__=="__main__":
    # 新建优惠券
    preConditionForTest().TestMysqlCoupon()
    # 新建红包
    preConditionForTest().createNewRedGift()
    # 取消客服所有订单
    preConditionForTest().cancleOrderFromSQL()