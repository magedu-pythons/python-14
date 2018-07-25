#!/usr/bin/env python
#author: Li Jinhzu
#
import random

lst = []
[lst.append(random.randrange(30)) for _ in range(20)]
print([sorted(lst,reverse=True)[i] for i in range(3)])
