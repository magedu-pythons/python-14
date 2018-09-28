# 1、python 中如何实现单例模式，尽可能多的写出实现方式


# 方法一：将单例类定义和实例化放在一个py文件中，使用时从该模块导入
class Singleton:
    def __init__(self):
        pass

    def foo(self):
        print('this is a singleton!')

singleton = Singleton()

# 方法二：使用装饰器
def Mysingleton(cls):
    _cls = []

    def _singleton(*args, **kwargs):
        if cls not in _cls:
            _cls.append(cls(*args, **kwargs))
        return _cls[0]
    return _singleton


@Mysingleton        # Singleton = mysingleton(Singleton)
class Singleton:
    def __init__(self, x):
        self.x = x

    def foo(self):
        print('this is a singleton!')

a = Singleton(2)
b = Singleton(3)
print(id(a))        # 56424176
print(id(b))        # 56424176
print(a.x)          # 2
print(b.x)          # 2

# 方法三 使用类方法实例化类,将类实例绑定到类属性上
import time
import threading
import logging

class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self, x):
        self.x = x
        time.sleep(1)

    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(Singleton, '_instance'):
            with Singleton._instance_lock:
                if not hasattr(Singleton, '_instance'):
                    Singleton._instance = Singleton(*args, **kwargs)
        return Singleton._instance

def task(args):
    obj = Singleton.instance(args)
    print(obj.x)
    logging.warning(obj)
for i in range(5):
    t = threading.Thread(target=task, args=(i,))
    t.start()

obj = Singleton.instance(1)
print(obj)                      # <__main__.Singleton object at 0x01283570>
obj = Singleton(1)
print(obj)                      # <__main__.Singleton object at 0x01283430>
# 次方法实例化类的时候必须使用类方法


# 方法四 使用__new__方法
import threading
import logging


class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, '_instance'):
            with Singleton._instance_lock:
                if not hasattr(Singleton, '_instance'):
                    Singleton._instance = object.__new__(cls)
        return Singleton._instance

obj1 = Singleton()
obj2 = Singleton()
print(obj1)
print(obj2)

def task():
    obj = Singleton()
    logging.warning(obj)
for i in range(5):
    t = threading.Thread(target=task)
    t.start()


# 方法五 使用metaclass方式实现
import threading


class Singleton(type):
    _instance_lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super(Singleton, cls).__call__(*args, **kwargs)

        return cls._instance


class Foo(metaclass=Singleton):
    def __init__(self, name):
        self.name = name


obj1 = Foo('name')
obj2 = Foo('name')
print(obj1, obj2)


