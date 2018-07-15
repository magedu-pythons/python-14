#!/usr/bin/env python
#.Author:Dyw
import random,string
num=string.ascii_letters + string.digits
passwd=[]
for n in range(200):
    for i in range(5):
        passwd.append(random.choice(num))
        passwds=''.join(passwd)
    passwd=[]
    print(passwds)
