#coding:utf-8
class person(object):
    '''
    This demo is used to get data from special test
    '''
    def __init__(self,sex,age):
        self.sex=sex
        self.age=age
    def __str__(self):
        if not isinstance(self.age,str):
            self.str_age=str(self.age)
        else:
            self.str_age=self.age
        person_all_msg=self.sex+' is {0} years old'.format(self.str_age)
        return person_all_msg
    @property
    def per_father(self):
        '''
        This is the person's father's age
        should add twenty years old
        :return: father's age
        '''
        self.father_age=self.age+20
        return self.father_age
    @classmethod
    def running(cls):
        print 'the person is running now！'

print person('boy',22)
print person('boy',22).per_father
print person.per_father.__doc__
print person.__doc__
p=person('boy',22)
print p.__dict__
p.running()