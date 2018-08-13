# 现有两元祖 (('a'),('b')),(('c'),('d')) ,请使用Python中的匿名函数生成列表 [ {'a':'c'｝,{'b':'d'}]
tuple1 = (('a'),('b'))
tuple2 = (('c'),('d'))

tup_all = tuple1, tuple2

lst = [(lambda tup, x: {tup[0][x]: tup[1][x]})(tup_all, x) for x in range(2)]  #定义一个匿名函数tup

print(lst)