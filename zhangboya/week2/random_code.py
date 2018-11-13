import random
s = set()
for i in range(200):
    c = 'abdfgjklmopq0123456789'
    ch = ''
    for n in range(6):
        ch += random.choice(c)
    s.add(ch)
print(s)