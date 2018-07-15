#!/usr/bin/env python
# author: Li Jinzhu

x = 0
y = 1

while y < 100:
    print(y, end=" ")
    x, y = y, x+y

