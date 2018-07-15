import random
count = 1
lst1 = []
lst1.append('iver1')
while count < 200:
    x = ''
    rd = random.sample('0123456789abcdefghijklmnopqrstuvwxz!', 5)
    for i in range(len(rd)):
        x += rd[i]
    if x not in lst1:
        lst1.append(x)
        count+=1
print(len(lst1), lst1)
