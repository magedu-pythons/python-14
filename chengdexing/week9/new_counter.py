# 1、请实现函数 new_counter ，使得调用结果如下：
#       c1 = new_counter(10)
#       c2 = new_counter(20)
#       print（c1(), c2(), c1(), c2()）
#       outputs ：
#       11 21 12 22


def new_counter(number: int):

    def x():
        nonlocal number
        number += 1
        yield number
    return x


c1 = new_counter(10)
c2 = new_counter(20)
print(next(c1()), next(c2()), next(c1()), next(c2()))



