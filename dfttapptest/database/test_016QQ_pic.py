#coding:utf-8
from selenium import webdriver
import time,os,requests
import xlrd,xlwt
from lxml import etree
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from xlutils.copy import copy
#使用selenium
#使用selenium的隐藏PhantimJS浏览器登陆账号后对内容获取
#注意frame与iframe的格式框切换
header={'User-Agent':"Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/45.0"}

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (header['User-Agent'])
driver = webdriver.PhantomJS(executable_path="E:\\mac\\id\\phantomjs-2.1.1-windows\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe",desired_capabilities=dcap)
driver.maximize_window()

def get_shuoshuo(qq,path):
    dict={'user':'2274052689',
          'psw':'992623wangx',
          'friend':'1508263737'
        }
    '''
    header = {'User-Agent':
                         'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36'
                        '(KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    '''
    testexist(path)
    try:
        driver.set_page_load_timeout(10)
        driver.get('http://user.qzone.qq.com/{}/311'.format(qq))
        time.sleep(3)
    except:
        print u'网页启动异常，请重新打开'
        time.sleep(2)
        driver.quit()
    try:
        driver.find_element_by_id('login_div')
    except:
        print u"非好友无法进入空间无权限抓取内容"
        driver.quit()
    else:
        #登录QQ空间
        driver.switch_to.frame('login_frame')
        driver.find_element_by_id('switcher_plogin').click()
        driver.find_element_by_id('u').clear()#选择用户名框
        driver.find_element_by_id('u').send_keys('2274052689')
        driver.find_element_by_id('p').clear()
        driver.find_element_by_id('p').send_keys('992623wangx')
        driver.find_element_by_id('login_button').click()
        time.sleep(3)
    driver.implicitly_wait(3)
    try:
        driver.find_element_by_id('QM_OwnerInfo_Icon')
    except:
        print u'空间加载异常，请重新打开'
        time.sleep(2)
        driver.quit()
    else:
        driver.find_element_by_link_text(u'相册').click()
        try:
            url_all='https://h5.qzone.qq.com/proxy/domain/tjalist.photo.qq.com/fcgi-bin/fcg_list_album_v3?g_tk=776706529&hostUin=%s&uin=%s&appid=4&inCharset=utf-8&outCharset=utf-8&source=qzone'%(dict['friend'],dict['user'])
            url_all='https://h5.qzone.qq.com/proxy/domain/tjalist.photo.qq.com/fcgi-bin/fcg_list_album_v3?g_tk=776706529&callback=shine0_Callback&t=681844228&hostUin=1508263737&uin=2274052689&appid=4&inCharset=utf-8&outCharset=utf-8&source=qzone&plat=qzone&format=jsonp&notice=0&filter=1&handset=4&pageNumModeSort=40&pageNumModeClass=15&needUserInfo=1&idcNum=5&callbackFun=shine0&_=1490612236877'
            rq=requests.get(url_all,headers=header)
            print rq.text

        except Exception,e:
            print e
            driver.quit()



def  testexist(path):
    if not os.path.exists(path):
        w= xlwt.Workbook()
        w.add_sheet('Sheet1')
        w.save(path)
    else:
        os.remove(path)
        w= xlwt.Workbook()
        w.add_sheet('Sheet1')
        w.save(path)

def write_data(data1,data2,path):
    f=xlrd.open_workbook(path)
    sheet=f.sheet_by_name('Sheet1')
    src=copy(f)
    row=sheet.nrows
    src.get_sheet(0).write(row,0,data1)
    src.get_sheet(0).write(row,1,data2)
    src.save(path)

if __name__ == '__main__':
   # work_path=raw_input(u'请输入存储数据路径--excle表格类型')2571278041
    work_path='E:\\0930\\meigege.xls'
    get_shuoshuo('1508263737',work_path)

