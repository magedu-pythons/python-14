import random
lst = ['a','b','c','d','e','f','g','h','!','@','#','$']
lst1 = []
lst2 = []
t = int(0)
while t < 200:
    lst1.append(''.join(random.sample(lst,5)))
    if lst2 not in lst1:
        lst2.append(lst1.pop())
        print (lst2[t])
        t += 1
