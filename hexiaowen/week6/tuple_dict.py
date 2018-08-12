tup1 = (('a'),('b'))
tup2 = (('c'),('d'))

#方法一
# foo = (lambda *args:{tup1[x]:tup2[x] for x in args})
# print(foo(*range(2)))

#方法二
foo = (lambda x,y:{x[c]:y[c] for c in range(len(x))})
print(foo(tup1,tup2))