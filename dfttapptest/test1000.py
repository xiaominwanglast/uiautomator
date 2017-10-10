#coding:utf-8
import random
file1=open(r'C:\Users\Administrator\Desktop\data\hh.txt','rb')
sss=file1.readlines(10000)
print len(sss)

M=input(u'人数：')
for i in range(M):
    file2=open(str(i)+'.txt','w')
    file2.close()

def run(txtname,ss):
    name=random.choice(txtname)
    file3=open(str(name)+'.txt','a+')
    print len(file3.readlines())
    write_data=ss.pop()
    if len(file3.readlines())<=len(sss)/M:
        file3.write(write_data)
        file3.close()
    else:
        txtname.pop(txtname.index(name))
        file3.close()
        run(txtname,ss)

for i in range(len(sss)):
    txtname=[i for i in range(M)]
    run(txtname,sss)


for i in range(4):
    file2=open(str(i)+'.txt','a+')
    print len(file2.readlines())
    file2.close()