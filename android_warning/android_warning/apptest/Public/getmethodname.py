#coding:utf-8
import inspect


class GetName(object):
    @classmethod
    def get_current_function_name(cls):
        return inspect.stack()[1][3]

