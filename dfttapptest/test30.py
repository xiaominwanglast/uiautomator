#coding:utf-8
ss=raw_input(u'sss：')
s=0
def run(i):
    global s
    print i
    s-=1
for i in range(int(ss)):
    run(i)
print s