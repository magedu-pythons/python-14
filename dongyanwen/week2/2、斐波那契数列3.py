#!/usr/bin/env python
#.Author:Dyw
a = 0
b = 1
c = a + b
while True:
    a = b
    b = c
    c = a + b
    if c < 100:
        print(c)
    else:
        break