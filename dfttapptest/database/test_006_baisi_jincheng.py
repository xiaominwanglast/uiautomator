#coding:utf-8
import requests
from requests.exceptions import HTTPError, ConnectionError
import re
import os,time
from multiprocessing import Process,JoinableQueue
class get_Url():
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

class ThreadUrl(Process):
    def __init__(self, queue):
        super(ThreadUrl, self).__init__()
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
#    work_List=list()
    queue=JoinableQueue()
    q=get_Url(10).get_pic()
    for i in q:
        queue.put(i)
    for i in range(10):
        t=ThreadUrl(queue)
  #      work_List.append(t)
        t.start()
    queue.join()
if __name__=='__main__':
    start = time.time()
    main()
    print("spend Time: %s" % (time.time() - start))