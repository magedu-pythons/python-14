#随机生成20个数字，并且筛选出其中最大的三个数

import random

lst=[random.randrange(0,101) for x in range(20)]
print(lst)
for i in range(3):
    max=i
    for j in range(i+1,20):
        if lst[max]<lst[j]:
            max=j

    print(lst[max])

    if max!=i:
        temp=lst[i]
        lst[i]=lst[max]
        lst[max]=temp



