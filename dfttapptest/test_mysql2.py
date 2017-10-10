#coding:utf-8

import MySQLdb
conn=MySQLdb.connect(host='localhost',user='root',passwd='123456',port=3306,charset="utf8")
cur=conn.cursor()
conn.select_db('test')

count=cur.execute('select * from xxxx')
print count

print cur.fetchone()
result=cur.fetchall()
print result

conn.commit()
cur.close()
conn.close()