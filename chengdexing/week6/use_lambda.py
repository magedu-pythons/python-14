# 现有两元祖 (('a'),('b')),(('c'),('d')) ,
# 请使用Python中的匿名函数生成列表 [ {'a':'c'｝,{'b':'d'}]

tup1 = (('a'),('b'))
tup2 = (('c'),('d'))


f = lambda x,y:[{k:v} for k,v in zip(x,y)]
print(f(tup1,tup2))