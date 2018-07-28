#!/usr/bin/env python
#.Author:Dyw
import random,string
num=string.ascii_lowercase
words = []
[words.append(random.choice(num)) for _ in range(10)]
print(words)
print(1) if 'x' in words else  print(0)