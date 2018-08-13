import random
def disorganize(lst):
    lens = len(lst)
    for i in range(lens):
            j = random.randint(0,lens-1)
            k = random.randint(0,lens-1)
            lst[j],lst[k]=lst[k],lst[j]
    return lst
print(disorganize([i for i in range(90)]))