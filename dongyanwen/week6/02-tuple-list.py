#!/usr/bin/env python
#.Author:Dyw
# 现有两元祖 (('a'),('b')),(('c'),('d')) ,请使用Python中的匿名函数生成列表 [ {'a':'c'｝,{'b':'d'}]
a="{0[0]}:{1[0]},{0[1]}:{1[1]}".format((('a'),('b')),(('c'),('d')))
print((lambda i,j : [{i} ,{j}] )(i=a[:3],j=a[4:]))