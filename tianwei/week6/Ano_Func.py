##现有两元组 (('a'),('b')),(('c'),('d')) ,请使用Python中的匿名函数生成列表 [ {'a':'c'｝,{'b':'d'}]

tup1=(('a'),('b'))
tup2=(('c'),('d'))

def makelist(tup1,tup2):
    aa, bb = tup1
    cc, dd = tup2
    lst=[{aa:cc},{bb:dd}]
    print(lst)

makelist(tup1,tup2)


print((lambda tup1,tup2 : [{tup1[i]:tup2[i]} for i in range(len(tup1)) if len(tup1)==len(tup2)] )( (('a'),('b')),(('c'),('d'))))


