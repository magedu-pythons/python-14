#第一种方法
lst = [1,1]
for i in range(2,100):
    lst[i] = lst[0] + lst[1]
    lst[0],lst[1] = lst[1],lst[i]
    lst.append(lst[i])

print(lst)


#第二种方法
f1 = f2 = 1
print(f1,f2,end='')
for i  in range(100):
    f3 = f1 + f2
    f1,f2 = f2,f3
    print(f3,end=' ')
