# 1.python中如何实现单例模式，尽可能多的写出实现方式
# 方法1,实现__new__方法
class Func1:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
a1 = Func1()
b1 = Func1()
print("方法1(__new__):", id(a1), id(b1))

# 方法2：使用装饰器实现
def deco(cls):
    instance = {}
    def _deco(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance
    return _deco
@deco
class Func2:
    def __init__(self):
        pass

a2 = Func2()
b2 = Func2()
print("方法2(装饰器):", id(a2),id(b2))

# 方法3：使用元类实现
class func3(type):
    instance = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls.instance:
            cls.instance[cls] = super().__call__(*args, **kwargs)
        return cls.instance

class Func3(metaclass=func3):
        pass

a3 = Func3()
b3 = Func3()
print("方法3(metaclass):", id(a3),id(b3))

# 方法4：使用共享状态和行为方法,使__dict__属性指向同一个字典
class func4:
    instance = {}
    def __new__(cls, *args, **kwargs):
        fn = super().__new__(cls, *args, **kwargs)
        fn.__dict__= cls.instance
        return fn
a5 = func4()
b5 = func4()
print("方法4(共享状态和行为):", id(a5.__dict__),id(b5.__dict__))






