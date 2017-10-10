#coding:utf-8
import redis
r=redis.Redis(host='127.0.0.1',port=6379,db=0)
#print r.info()
print r.dbsize()
print r.ping()
#r.set('dingdian:start_urls','ddd')
print r.get('dingdian')
li=['name','start_urls']
print r.mget(li)
print r.getrange('start_urls',0,3)
r.mget({"name1":'zhangsan', "name2":'lisi'})
print r.get('name2')
print r.llen('dingdian:start_urls')
r.rpushx('dingdian:start_urls','sss')
#print r.lrange('dingdian:start_urls',0,r.llen('dingdian:start_urls'))
print r.lpop('dingdian:start_urls')
print r.blpop('dingdian:start_urls',3)