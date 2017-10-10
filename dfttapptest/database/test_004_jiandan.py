#coding:utf-8
import requests
import bs4
import os,sys
reload(sys)
sys.setdefaultencoding('utf-8')
#模拟header信息，保证网络请求通过
#主要使用bs4的Beautifulsoup来规范框架
header = {'User-Agent':
                         'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36'
                        '(KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
         }
def req(start_page,end_page):
# 生成图片地址的空列表
    fecthed_pic_add_all = []
# 逐一访问页面
    for i in range(start_page,end_page+1):
         jiandan_url = 'http://jandan.net/ooxx/page-'+str(i)
        #防止请求错误
         try:
             response = requests.get(jiandan_url,headers=header)
          #   print response.raise_for_status()
         except Exception as e:
             print(u'请求出现错误，错误信息：%s' %e)
         else:
             #确定访问正常后，得到页面信息
             content = response.text
             #将信息传入bs4
             fecthed_info = bs4.BeautifulSoup(content,'html.parser')
             #寻找所有包含图片地址的tag
          #   print fecthed_info
             fecthed_info_tagA = fecthed_info.find_all('a',class_='view_img_link')
             #得到本页所有图片地址
             fecthed_pic_add = [l.get('href') for l in fecthed_info_tagA]
             #将该页面图片地址添加到总表
             for i in fecthed_pic_add:
                  fecthed_pic_add_all.append(i)
    #返回图片地址列表
    # print (fecthed_pic_add_all)
    return fecthed_pic_add_all
#下载图片
def downliad_pic(pic_addresses,path):
     #遍历图片地址
     for i in pic_addresses:
         try:
             i = 'http:'+i
             #请求图片网址
             pic_resp = requests.get(i,headers = header)
             #二进制方式读取网页
             pic = pic_resp.content
             pic_name = i.split('/')[-1]
             print pic_name
             #以'wb'写入文件
             with open(path+'\\'+pic_name,'wb') as f:
                 f.write(pic)
                 print (u'文件\t'+pic_name+'\t已下载')
         except Exception as e:
            print(u'下载出现错误，信息：%s' %e)
def main(path):
    start_page,end_page=0,0
    #判断是否创建下载文件夹
    create_file = os.path.exists(path)
    #print(create_file)
    if not create_file:
        os.mkdir(path)
    print (u'设置您要下载的开始页与最终页：')
    while True:
        try:
            start_page = int(input(u'起始页：'))
            end_page = int(input(u'最终页：'))
            if end_page < start_page:
                print (u'最终页小于起始页')
                continue
        except:
            print (u'输入不合法')
        else:
            break
    print (u'正在下载...')
    pic_addresses = req(start_page, end_page)
    downliad_pic(pic_addresses,path)
    print (u'全部下载完成')

path='E:\\os\\jianbing'
main(path)
