import random

list1 = []
dict1 = {}
for i in range(10):
    list1.append(i)
for i in range(65, 91):
    list1.append(chr(i))
for i in range(97, 123):
    list1.append(chr(i))

def code(i):
    dict1[i] = str1()
    if i > 0:
        j = 0
        while j < i:
            if dict1[i] == dict1[j]:
                dict1[i] = str1()
                j = 0
            j += 1

def str1():
    y = ''
    for j in range(8):
        y += str(random.choice(list1))
    return y

for i in range(200):
    code(i)
for i in range(200):
    print(dict1[i])
