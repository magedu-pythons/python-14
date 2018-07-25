#给出任意一个列表，请查找出x元素是否在列表里面，如果存在返回1，不存在返回0


def searchx(lis, x):
    for i in lis:
        if i == x:
            return 1
            break
    else:
        return 0

list = input ("list : ")
x = input ("x : ")
y = searchx(list, x)
print(y)

