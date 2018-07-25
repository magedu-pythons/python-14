import random
lst=[]
for i in range(20):
    lst.append(random.randint(1,1000))
print(lst)
for i in range(3):
    for j in range(20-i-1):
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1]=lst[j+1],lst[j]
print(lst[-1],lst[-2],lst[-3])