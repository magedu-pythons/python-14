#!/usr/bin/env python
#.Author:Dyw
a,b = 0,1
print(a,'\n',b,'\n',a+b,sep='')
n = int(input("请输入正整数："))
for i in range(n):
    a,b=b,(a+b)
    c = a + b
    if c < 100:
        print(c)
    else:
        break