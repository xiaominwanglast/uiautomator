#coding:utf-8
'''
class obe(object):
    pass
MyShinyClass = type('obe', (), {})
print MyShinyClass
print hasattr(obe, 'new_attribute')
obe.new_attribute='foo'
print hasattr(obe, 'new_attribute')
print obe.new_attribute

def choose_class(name):
    if name == 'foo':
        class Foo(object):
            pass
        return Foo # 返回的是类，不是类的实例
    else:
        class Bar(object):
            pass
        return Bar
Myclass=choose_class('gg')
print Myclass
'''
'''
def foo(x):
    print "executing foo(%s)"%(x)

class A(object):
    def foo(self,x):
        print "executing foo(%s,%s)"%(self,x)

    @classmethod
    def class_foo(cls,x):
        print "executing class_foo(%s,%s)"%(cls,x)

    @staticmethod
    def static_foo(x):
        print "executing static_foo(%s)"%x

a=A()
a.foo('s')
a.class_foo('s')
a.static_foo('s')
'''
def print_everything(*args):
        for count, thing in enumerate(args):
            print '{0}. {1}'.format(count, thing)
print_everything('apple', 'banana', 'cabbage')
def table_things(**kwargs):
    for name, value in kwargs.items():
        print '{0} = {1}'.format(name, value)
table_things(apple = 'fruit', cabbage = 'vegetable')