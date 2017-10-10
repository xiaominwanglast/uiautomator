#coding:utf-8
import urllib2,json,requests
#获取access_token
def token():
    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' %('wx2298747f1280d230', 'be86f9b8a720f6bd0a2ba4cb8f5c560d')
    rq=requests.get(url)
    js=json.loads(rq.text)
    return js['access_token']
access=token()
#获取media_id
url1='http://file.api.weixin.qq.com/cgi-bin/material/add_material?access_token=%s'%access
#url2='http://file.api.weixin.qq.com/cgi-bin/media/upload?access_token=%s&type=TYPE'%access
with open('E:\\APP\\pic_meta\\timthumb.jpg','rb') as fs:
    content=fs.read()
rq1=requests.post(url1,data={'media':content,'type':'thumb'})
print rq1.text


'''
access_url='https://api.weixin.qq.com/cgi-bin/material/add_news?access_token=ACCESS_TOKEN'
data={"articles": [{
       "title": u'利用新接口抓取微信公众号的所有文章',
       "thumb_media_id": 'http://cuiqingcai.com/wp-content/themes/Yusi/timthumb.php?src=http://qiniu.cuiqingcai.com/wp-content/uploads/2016/03/34.jpg&h=123&w=200&q=90&zc=1&ct=1',
       "author": 'jingmi',
       "digest": DIGEST,
       "show_cover_pic": 1,
       "content": CONTENT,
       "content_source_url": 'http://cuiqingcai.com/4652.html'
    },
 ]
}
'''
