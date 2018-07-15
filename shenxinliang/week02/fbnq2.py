i = 1
def fbnq(i):
    if (i == 1 or i == 2):
        return 1
    else:
        return int(fbnq(i-1) + fbnq(i-2))  #使用递归进行输出
while i:
    s = fbnq(i)
    if s < 100:   #通过s的临界条件决定数列打印范围
        print(s, end=' ')
    else:
        break
    i += 1