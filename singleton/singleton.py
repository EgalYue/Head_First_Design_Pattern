# -*- coding: utf-8 -*-
# @FileName: singleton.py
# @Author  : Yue Hu
# @E-mail  : yue.hu@ninebot.com

# 1.

class Singleton(object):
    def foo(self):
        pass
singleton = Singleton()


# 2.
def Singleton(cls):
    _instance = {}

    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]

    return _singleton


@Singleton
class A(object):
    a = 1

    def __init__(self, x=0):
        self.x = x


a1 = A(2)
a2 = A(3)
print a1.a
print a1.x
print a2.a
print a2.x


# 3.

class Singleton(object):

    def __init__(self):
        pass

    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            Singleton._instance = Singleton(*args, **kwargs)
        return Singleton._instance
