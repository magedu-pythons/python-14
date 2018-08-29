#!/usr/bin/env python
#.Author:Dyw
#!/usr/bin/env python
#.Author:Dyw
# 1、请实现函数 new_counter ，使得调用结果如下：
#       c1 = new_counter(10)
#       c2 = new_counter(20)
#       print（c1(), c2(), c1(), c2()）
#       outputs ：
#       11 21 12 22
def new_counter(i):
    def counter():
        nonlocal i
        while True:
            i += 1
            yield i
    c = counter()
    return lambda : next(c)
c1 = new_counter(10)
c2 = new_counter(20)
print(c1(),c2(),c1(),c2())

# 2、实现一个函数，输入字符串，判断该字符串是否不含有重复字符
def foo():
    str = input("input str:")
    _set = set(str)
    print('no Duplicate strings') if len(str) == len(_set) else print("Duplicate strings")
foo()
