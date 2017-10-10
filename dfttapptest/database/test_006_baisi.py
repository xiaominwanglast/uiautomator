#coding:utf-8
import requests
from requests.exceptions import HTTPError, ConnectionError
import threading
from bs4 import BeautifulSoup
import re
import os,time
import Queue

class get_Url:
    def __init__(self,num):
        self.num=num
        self.headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
        self.url='http://www.budejie.com/pic/{}'
        self.url_all=[]

    def get_pic(self):
        for i in range(1,self.num):
            try:
                rq=requests.get(self.url.format(i),headers=self.headers,timeout=5)
                pt = r'data-original="(\w.+?\.\w+)" title='
                url_list= re.findall(re.compile(pt),rq.text)
                for url in url_list:
                    self.url_all.append(url)
            except HTTPError as e:
                print e
            except ConnectionError as e:
                print e
        return self.url_all
    @staticmethod
    def geturl(url):
        print url

class ThreadUrl(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0",
        }
        self.workpath='E:\\os\\baisi_mp4'
    def run(self):
        while not self.queue.empty():
            url_name = self.queue.get()
            print u'正在下载%s'%url_name
            name=os.path.basename(url_name)
            with open(self.workpath+'\\'+name,'wb') as ps:
                ps.write(requests.get(url_name,headers=self.headers).content)
            self.queue.task_done()

def main():
    queue=Queue.Queue()
    p=get_Url(10).get_pic()
    for i in p:
        queue.put(i)

    for t in range(10):
        t=ThreadUrl(queue)
        t.setDaemon(True)
        t.start()
    queue.join()

if __name__=='__main__':
    start = time.time()
    main()
    print("spend Time: %s" % (time.time() - start))

'''
    "http1": "http://119.190.214.134:8118",
    "http2": "http://124.88.67.24:80",
    "http3": "http://101.53.101.172:9999",
    "http4": "http://115.29.2.139:80",
    "http5": "http://124.88.67.20:80"
'''


def get_mp4(path,num):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    url='http://www.budejie.com/video/{}'
    for i in range(1,num):
        rq=requests.get(url.format(num),headers=headers)
        bs=BeautifulSoup(rq.text,'html.parser')
        data=bs.find_all('div',class_='j-video')
        fecthed = [(l.get('data-mp4'),l.get('data-id')) for l in data]
        for mp in fecthed:
            with open(path+'\\'+str(mp[1]+'.mp4'),'wb') as fs:
                fs.write(requests.get(mp[0],headers=headers).content)
path='E:\\os\\baisi_mp4'
get_mp4(path,2)


