#coding:utf-8

import MySQLdb  #加载mysql数据库模块

conn = MySQLdb.connect(host='localhost',port=3306,user='root',passwd='123456') #连接 MYSQL 数据库
cur = conn.cursor()
conn.select_db('test')
#cur.execute('create table xxxx(id int,info varchar(20))')

value=[1,'hi rollen']
cur.execute('insert into xxxx values(%s,%s)',value)
values=[]
for i in range(20):
        values.append((i,'hi rollen'+str(i)))
cur.executemany('insert into xxxx values(%s,%s)',values)
cur.execute('update xxxx set info="I am rollen" where id=3')
aa=cur.execute('select * from xxxx')
print cur.fetchone()
for i in cur.fetchmany(aa):
        print i
conn.commit()  # 提交数据库
cur.close() # 关闭游标
conn.close()   # 关闭连接