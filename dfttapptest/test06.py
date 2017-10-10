#coding:utf-8
import logging
import sys

l_g = logging.getLogger('ss')
l_g.setLevel(logging.ERROR) #日志等级为ERROR

s_h = logging.StreamHandler(sys.stderr)
l_g.addHandler(s_h)


l_g.info('dddd') #输出等级为info
