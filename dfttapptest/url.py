#coding:utf-8
import requests,urllib,urllib2
import bs4,csv
import pymongo
def geturl():
	#连接数据库
	conn = pymongo.MongoClient('localhost',27017) #连接上数据库的数据流
	cn=conn.qimengjiaoyu
	table=cn.dataTB
	#清除数据
	table.remove({})
	#中文搜索转码
	url_name=u'职业启蒙教育'
	url_name=url_name.encode('utf-8')
	url1=urllib2.quote(url_name)
	for page in range(0,66):
		print u'正在下载第%s页面'%(page+1)
		url='http://xueshu.baidu.com/s?wd={}&pn={}&tn=SE_baiduxueshu_c1gjeupa'.format(url1,10*page)
		rq=requests.get(url)
		bs=bs4.BeautifulSoup(rq.text,'html.parser')
		div=bs.find_all('div',class_='result sc_default_result xpath-log')
		for i in div:
			data={}
			title=i.find_all(['a','data-click'])
			body=i.find_all('div',class_="c_abstract")
			stime=i.find_all('span',class_="sc_time")
			data['name']=''.join([str for str in title[0].stripped_strings])
			data['href']='http://xueshu.baidu.com'+title[0].attrs['href']
			word=''.join([str for str in body[0].stripped_strings])
			if len(word.split(u'来源：'))==2:
				data['word']=word.split(u'来源：')[0]
				data['resource']=word.split(u'来源：')[1]
			else:
				data['word']=word.split(u'来源：')[0]
				data['resource']='No'
			if stime:
				data['fortime']=stime[0].string
			else:
				data['fortime']='No'
			table.insert_one(data)
def write():
	#连接数据库
	conn = pymongo.MongoClient('localhost',27017) #连接上数据库的数据流
	cn=conn.qimengjiaoyu
	table=cn.dataTB

	csvfile = open('qimeng.csv','wb')
	writer = csv.writer(csvfile)
	#csv写入数据
	for data in table.find():
		writer.writerow([data['name'].encode('utf-8'),data['word'].encode('utf-8'),data['fortime'],data['resource'].encode('utf-8'),data['href']])

if __name__=='__main__':
	#geturl()
	write()

