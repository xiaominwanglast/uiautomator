#coding:utf-8
import requests
import pymongo
cn=pymongo.MongoClient(host='127.0.0.1',port=27017)
db=cn.dfttcomment
table=db.yingyongbaocommenttable
import time
import json
header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.6 Safari/537.36'}
'''
#360助手
for i in  range(0,4000,20):
    print u'测试页面为第%d页'%(i/20)
    url='http://comment.mobilem.360.cn/comment/getComments?baike=%E4%B8%9C%E6%96%B9%E5%A4%B4%E6%9D%A1+Android_com.songheng.eastnews&c=message&a=getmessage&start={0}&count=20'.format(i)
    rq=requests.get(url,headers=header)
    js=json.loads(rq.text)
    for data in js['data']['messages']:
        table.save({'username':data['username'],'score':data['score'],'_id':data['msgid'],'content':data['content'],
                      'qid':data['qid'],'create_time':data['create_time'],'model':data['model'],'version_name':data['version_name']})
    time.sleep(1)
'''
def rq(test_url):
    rq_t=requests.get(test_url,headers=header)
    time.sleep(1)
    js_t=json.loads(rq_t.text)
    return js_t
for i in range(100):
    print i
    url='http://sj.qq.com/myapp/app/comment.htm?apkName=com.songheng.eastnews&apkCode=71&p={}&fresh=&contextData='.format(i)
    #{u'count': None, u'obj': None, u'success': False, u'pageSize': None, u'msg': u'CommentManager.takeCommentList.error', u'total': None, u'pageContext': None}
    js_data=rq(url)
    while not js_data['obj']:
        js_data=rq(url)
    for data in js_data['obj']['commentDetails']:
        table.save({'uin':data['uin'],'createdTime':time.strftime('%Y-%m-%d,%H:%M',time.localtime(data['createdTime'])),
                    'content':data['content'],'score':data['score'],'nickName':data['nickName'],'versionCode':data['versionCode']})



