#coding:utf-8
'''
def deco(func):
    def _deco():
        print 'before:'
        res=func()
        print 'next:'
        return res
    return _deco

@deco
def myfunc():
    print 'do'
    return 'ok'
print myfunc()

def deco(func):
    def _deco(a,b):
        print 'before:'
        res=func(a,b)
        print 'next:'
        return res
    return _deco
@deco
def myfunc(a,b):
    print 'a:{0},b:{1}'.format(a,b)
    return a+b

print myfunc(1,2)
'''
def deco(arg):
    def _deco(func):
        def __deco():
            print 'before:'
            print func.__name__,arg
            func()
            print func.__name__,arg
            print 'next:'
        return __deco
    return _deco

@deco('mymodule')
def myfunc():
    print 'ok'

myfunc()