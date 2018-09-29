# 2.两个有序数组，分别拥有m和n的长度，求其合并后的的第k个值
def find_val(lst1, lst2, k):
    try:
        lst1 = lst1 + lst2
        lst1.sort()
        print("合并数组：{}".format(lst1))
        print("第{}个值为：{}".format(k, lst1[k-1]))
    except:
        print("第{}个值不在合并数组范围内".format(k))


lst1 = [1, 3, 5, 7, 9]
lst2 = [2, 3, 4, 5, 6, 8, 10]
while True:
    try:
        k = int(input("请输入返回第几个值（k>0）："))
        if k > 0:
            break
    except:
        continue

find_val(lst1,lst2,k)
