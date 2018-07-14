# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 10:46:59 2018

@author: Administrator
"""

a = 1
b = 1
print(a)
while True:
    a, b = b, a+b
    print(a)
    if b >= 100:
        break