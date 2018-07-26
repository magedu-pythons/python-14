import random
lst1 = [chr(i) for i in range(97,123)]
lst2 = [chr(i) for i in range(65,90)]
lst = lst1+lst2
for i in range(0,10):
    lst.append(str(i))
s = ''
x = 1
while x:
    for j in range(6):
        n = random.choice(lst)
        s = s + n
    print(s)
    s = ''
    x += 1
    if x == 201:
        break
