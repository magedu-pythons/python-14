# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 10:47:52 2018

@author: Administrator
"""


fibo = [1, 1]
while True:
    num = fibo[len(fibo)-1] + fibo[len(fibo)-2]
    fibo.append(num)
    if fibo[len(fibo)-1] > 100:
        fibo.pop(len(fibo)-1)
        break
    
    
        


print(fibo)
