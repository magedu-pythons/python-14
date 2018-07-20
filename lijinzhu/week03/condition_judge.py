#!/usr/bin/env python
#author: Li Jinzhu

lst = ['a','s','d','f','g',3,6,4,7,9]
_lst = input("input >>> : ")

if _lst.isdigit():
    _lst = int(_lst)

print(0 if _lst in lst else 1)
