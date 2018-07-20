


lst = list(range(100))
x = int(input("请输入要查找的数: "))
try:
    if lst.index(x):
        print(1)
except ValueError as e:
    print(0)



