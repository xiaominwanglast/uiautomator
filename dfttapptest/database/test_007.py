#coding:utf-8
import requests,json
from lxml import etree
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
url='http://www.huya.com/cache.php?m=LiveList&do=getLiveListByPage&gameId=1&tagAll=0&page=1'
rq=requests.get(url,headers=headers)
js=json.loads(rq.text)
for i in js['data']['datas']:
    print i['roomName'].encode('gb18030')
    print i['nick'].encode('gb18030')
    print i['introduction'].encode('gb18030')
    print i['uid'],i['totalCount'],i['gameHostName'],i['gameFullName']


'''
url = 'http://www.huya.com/g/lol'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
res = requests.get(url,headers=headers).text
s = etree.HTML(res)
list_data=s.xpath('//i[@class="nick"]/text()')
for i in list_data:
    print i
'''