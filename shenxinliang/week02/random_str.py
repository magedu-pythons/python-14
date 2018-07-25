import random

count = 0
s1 = set()
while True:
    s = 'abcdefghjkl1234567890'
    ys = ''
    for i in range(5):
        ys += random.choice(s)
        print(ys)

    s1.add(ys)

    if len(s1) == 200:
        break

print(s1)