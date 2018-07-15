#!/usr/bin/env python
#.Author:Dyw
def fibo(n):
    a = 0
    b = 1
    if n == 1 or n == 2 :
        return n
    return fibo(n-1)+fibo(n-2)
n=int(input("输入想得知的第几个数字>>:"))
print(fibo(n))