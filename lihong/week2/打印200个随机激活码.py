#打印200个随机激活码
import random
lst=[]
count=0
while True:
    i=random.randint(10000,99999)
    if i not in lst:
        lst.append(i)
        count+=1
        if count>=200:
            break
print(lst)