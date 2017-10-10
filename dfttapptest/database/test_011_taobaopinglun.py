#coding:utf-8
import requests
import json,time
import simplejson

headers = {
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:51.0) Gecko/20100101 Firefox/51.0'}
base_url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=38975978198&spuId=279689783&sellerId=92889104&order=3&callback=jsonp698'
#在base_url后面添加&currentPage=1就可以访问不同页码的评论
for i in range(1, 5, 1):
    url = base_url + '&currentPage=%s' % str(i)
    #将响应内容的文本取出
    print url
    tb_req = requests.get(base_url, headers=headers).text[12:-1]
    #将str格式的文本格式化为字典
    try:
        tb_dict = simplejson.loads(tb_req)
    except Exception as e:
        print e
    else:
        #编码： 将字典内容转化为json格式对象
        tb_json = json.dumps(tb_dict, indent=2)   #indent参数为缩紧，这样打印出来是树形json结构，方便直观
        #解码： 将json格式字符串转化为python对象
        review_j = json.loads(tb_json)
        for p in range(1, 20,1):
            print(review_j["rateDetail"]["rateList"][p]['rateContent'])
        time.sleep(1)
'''
#将响应内容的文本取出
tb_req = requests.get(base_url, headers=headers).text[13:-1]

#将str格式的文本格式化为字典
tb_dict = simplejson.loads(tb_req)
#编码： 将字典内容转化为json格式对象
tb_json = json.dumps(tb_dict, indent=2)   #indent参数为缩紧，这样打印出来是树形json结构，方便直观


#解码： 将json格式字符串转化为python对象
review_j = json.loads(tb_json)
print review_j

#这里的0是当前页的第一个评论，每页面其实是有20个评论的
print(review_j["rateDetail"]["rateList"][0]['rateContent'])
'''