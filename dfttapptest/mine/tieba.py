#coding:utf-8
import requests
import re
import os
import time
import random
from bs4 import BeautifulSoup
from pymongo import MongoClient
class Tool():
    removeImg = re.compile('<img.*?>|｛7｝|&nbsp;')
    removeAddr = re.compile('<a.*?>|</a>')
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    replaceTD = re.compile('<td>')
    replaceBR = re.compile('<br><br>|<br>|</br>|</br></br>')
    removeExtraTag = re.compile('.*?')
    removeNoneLine = re.compile('\n+')
    def replace(self, x):
        x = re.sub(self.removeImg, "", x)
        x = re.sub(self.removeAddr, "", x)
        x = re.sub(self.replaceLine, "\n", x)
        x = re.sub(self.replaceTD, "\t", x)
        x = re.sub(self.replaceBR, "\n", x)
        x = re.sub(self.removeExtraTag, "", x)
        x = re.sub(self.removeNoneLine, "\n", x)
        return x.strip()



class Spider():
    def __init__(self):
        self.tool = Tool()
        self.work_path='E:\Desktop\code\LvXingTieBa'
        #初始化连接数据库
        self.cn=MongoClient(host='127.0.0.1',port=27017)
        self.db=self.cn.job
        self.table=self.db.tieba
        self.table.remove({})

    def getSource(self,url):
        user_agents=['Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20130406 Firefox/23.0',
                     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0',
                     'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533+ \(KHTML, like Gecko) Element Browser 5.0',
                     'IBM WebExplorer /v0.94', 'Galaxy/1.0 [en] (Mac OS X 10.5.6; U; en)',
                     'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
                     'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14',
                     'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) \Version/6.0 Mobile/10A5355d Safari/8536.25',
                     'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) \Chrome/28.0.1468.0 Safari/537.36',
                     'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0; TheWorld)']
        index=random.randint(0,8)
        user_agent=user_agents[index]
        headers = {'User_agent': user_agent}
        html=requests.get(url,headers=headers)
        return html.text

    #获取帖子标题
    def getTitle(self,url):
        result=self.getSource(url)
        items=re.findall(r'<title>(.*?)</title>',result)
        print u'这篇帖子标题为：',self.tool.replace(items[0])

    #获取帖子总页数
    def getPageNumber(self,url):
        result=self.getSource(url)
        pattern=re.compile('<ul.*?l_posts_num.*?<span class="red">(.*?)</span>',re.S)
        items=re.search(pattern,result).group(1)
        print u'帖子共有%s页'%items
        return items

    #获取评论内容
    def getContent(self,url):
        result = self.getSource(url)
        pattern=re.compile('<a data-field.*?p_author_name.*?">(.*?)</a>.*?<div id="post_content_.*?>(.*?)</div>',re.S)
        items=re.findall(pattern,result)
        number = 1
        for item in items:
            tieba_dict={}
            try:
                print u'\n', number, u'楼', u'\n楼主：', item[0], u'\n内容:', self.tool.replace(item[1])
                tieba_dict['number']=str(number)+u'楼'
                tieba_dict['name']=item[0]
                tieba_dict['body']=self.tool.replace(item[1])
                self.table.insert_one(tieba_dict)
            except:
                pass
            time.sleep(0.01)
            number += 1

    #获取晒图,清洗获得链接并保存入list
    def getImage(self,url):
        result=self.getSource(url)
        soup=BeautifulSoup(result,'lxml')
        #此处用BeautifulSoup显然更高效
        #find_all()返回一个list,find()返回一个元素
        #注意class属性和python内置的重合，所以加_变成class_
        items=soup.find_all('img',class_="BDE_Image")
        images=[]
        number=0
        for item in items:
            print u'发现一张图，链接为:',item['src']
            images.append(item['src'])
            number+=1
        if number>=1:
            print u'\n',u'共晒图',number,u'张，厉害了我的哥！！！'
        else:
            print u'喏，没有图......'
        return images

    #创建目录
    def makeDir(self,path):
        self.path=path.strip()
        E=os.path.exists(os.path.join(self.work_path, self.path))
        if not E:
            #创建新目录,若想将内容保存至别的路径（非系统默认），需要更环境变量
            #更改环境变量用os.chdir()
            os.makedirs(os.path.join(self.work_path, self.path))
            os.chdir(os.path.join(self.work_path, self.path))
            print u'正在创建名为',self.path,u'的文件夹'
            return self.path
        else:
            print u'名为',self.path,u'的文件夹已经存在...'
            return False

    #万水千山走遍，接下来就是保存美图
    def saveImage(self,detailURL,name):
        try:
            data=requests.get(detailURL,timeout=10).content
            #保存文件，一定要用绝对路径      `
            #所以设置self.path，是为了方便后面函数无障碍调用
        except requests.exceptions.ConnectionError:
            print u'下载图片失败'
            return None
        fileName = name + '.' + 'jpg'
        f=open(r'E:\Desktop\code\LvXingTieBa\%s\%s'%(self.path,fileName),'wb')
        f.write(data)
        f.close()
        print u'成功保存图片',fileName

    #集合所有的操作,并获取多页
    def getAllPage(self,Num):
        self.siteURL = 'http://tieba.baidu.com/p/' + str(Num)
        #获取帖子标题
        self.getTitle(self.siteURL)
        #获取帖子页数
        numbers=self.getPageNumber(self.siteURL)
        for page in range(1,int(numbers)+1):
            #格式化索引链接
            self.url=self.siteURL+'?pn='+str(page)
            print u'\n\n',u'正准备获取第',page,u'页的内容...'
            #获取评论
            print u'\n',u'正准备获取评论...'
            self.getContent(self.url)
            #每一页创建一个文件
            self.makeDir(path='page'+str(page))
            #获取图片
            print u'\n',u'正准备获取图片...'
            images=self.getImage(self.url)
            print u'\n',u'正准备保存图片...'
            number=1
            #保存图片，先从之前的list中找链接
            for detailURL in images:
                name='page'+str(page)+'num'+str(number)
                self.saveImage(detailURL,name)
                time.sleep(0.1)
                number+=1

            print u'\n\n',u'完成第',page,u'页'
        print u'\n\n',u'恭喜，圆满成功！'

#raw_input()实现和外部交互，想看哪个贴就看哪个贴
Num=int(raw_input(u'您好，输入帖子号：'))
spider=Spider()
spider.getAllPage(Num)



