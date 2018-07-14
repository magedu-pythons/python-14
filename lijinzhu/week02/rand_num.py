#!/usr/bin/env python

import random

code=' '

for _ in range(200):
    for i in range(5):
        add=random.choice([random.randrange(10),chr(random.randrange(65,91))])
        code += str(add)
    print(code)
    code=' '

