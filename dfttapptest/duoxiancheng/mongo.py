#coding:utf-8
import pymongo
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
#连接mongodb
#cn=MongoClient()
#cn=MongoClient('localhost',27017)
cn=MongoClient(host='127.0.0.1',port=27017)

#创建数据库
db=cn.test1
collection_set01=db.try1
record_l = [
{'_id':0,'name': 'zzzzz','age': -27,'high': 176},
{'_id':1,'name': 'zhangweijian','age': 27,'high': 171},
{'_id':2,'name': 'zhang','age': 26,'high': 173},
{'_id':3,'name': 'wei','age': 29,'high': 180},
{'_id':4,'name': 'weijian','age': 30,'high': 158},
{'_id':4,'name': 'zhangjian','age': 22,'high': 179},
{'_id':6,'name': 'zwj','age': 19,'high': 166},
{'_id':100,'name': 'zwj','age': 19,'list':[2,3,5]},
{'_id':101,'name': 'zwj','age': 19,'list':{'url':'www.baidu,com','name':u"首页"}},
]
try:
    for record in record_l:
        collection_set01.save(record)
except pymongo.errors.DuplicateKeyError:
    print 'record exists'
except Exception as e:
    print e
'''
#table1.insert_one(data)
table.update({'name':u'张三'},{"$set":{'age':30}})
for i in table.find({"name": u"张三"}):
    print i
table.remove({'name':u'张三'})
table1.profiles.create_index([('user_id', pymongo.ASCENDING)],unique=True)
user_profiles = [
{'user_id': 211, 'name': 'Luke'},
{'user_id': 212, 'name': 'Ziltoid'}]
#insert_many是数组
result = table1.insert_many(user_profiles)
#删除所有数据
#table1.remove({})
'''