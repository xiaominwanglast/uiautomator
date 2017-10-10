#coding:utf-8'
def do(out_time=3):
    if out_time>1:
        out_time-=1
        print out_time
        do(out_time=out_time)
do()