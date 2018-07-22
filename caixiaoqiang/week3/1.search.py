lst1 = [1, 22, 12, 5, 6, 45, 16, 12, 5, 67, 13]
x = int(input("请输入查询元素x:"))
flag = 0
for i in lst1:
    if x == i:
        flag = 1
        break
print(flag)


