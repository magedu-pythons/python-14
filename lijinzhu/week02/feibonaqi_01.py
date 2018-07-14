#!/usr/bin/env python
#author: Li Jinzhu

lst = [1, 1]

for i in range(2,100):
    lst.append(lst[i-2] + lst[i-1])
    if lst[i] >= 89:
        break

print(lst)
