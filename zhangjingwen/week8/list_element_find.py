# 2、给定一个整型列表，请实现从其中找出2个数的和为某一个指定的值？
# 如：lst =[1,5,2,7,4,9]，指定的目标值为11，可以从中找出 2和9之和为11
"""思路：利用中值折半，减少遍历次数。"""


def element_find(src: list, num: int):
    new = src.copy()
    new.append(num/2)
    new.sort()
    index = new.index(num/2)

    while len(src) >= 2:
        result = []
        count = 0       # 迭代次数统计
        for i in range(index):
            for j in range(index+1, len(new)):
                count += 1
                if new[i]+new[j] == num:
                    result.append((new[i], new[j]))
        return (result, count) if result else None
    else:
        return


'''test'''
print(element_find([-1, -2, 0, 8, 5, 7, 9, 2, 5, 25, 14, 3], 8))    # ([(-1, 9), (0, 8), (3, 5), (3, 5)], 35)
print(element_find([-1, -2, 0, 8, 5, 7, 9], 8))                     # ([(-1, 9), (0, 8)], 12)
print(element_find([-1, -2, 0, 8, 5, 7, 9], 10))                    # None
print(element_find([2], 10))                                        # None
print(element_find([1, 5, 2, 7, 4, 9], 11))                         # ([(2, 9), (4, 7)], 8)

# -----------------------------------------分割线------------------------------------------------------
# 方法二
'''思路：利用0、num/2、num三个数将原列表切分成四段，0之前的与num之后的组合迭代；0~num/2的与num/2~num组合迭代'''


def element_find(src: list, num: int):
    while len(src) >= 2:
        new = src.copy()
        new.extend([0, num / 2, num])
        new.sort()
        for x, y in enumerate(new):
            if y > 0:
                index1 = x-1
                break
        index2 = new.index(num / 2)
        index3 = new.index(num)

        count1 = 0
        count2 = 0          # 迭代次数统计
        result = []
        if new[:index1] and new[index3+1:]:
            for i in range(index1):
                for j in range(index3+1, len(new)):
                    count1 += 1
                    if new[i]+new[j] == num:
                        result.append((new[i], new[j]))

        if new[index1+1:index2] and new[index2+1:index3]:
            for m in range(index1+1, index2):
                for n in range(index2+1, index3):
                    count2 += 1
                    if new[m]+new[n] == num:
                        result.append((new[m], new[n]))

        return (result, count1+count2) if result else None
    else:
        return


'''test  总结：在列表规模较大、正负数均存在时，方法二能够减少更多的迭代次数，效率更高'''
print(element_find([-1, -2, 0, 8, 5, 7, 9, 2, 5, 25, 14, 3], 8))   # ([(-1, 9), (0, 8), (3, 5), (3, 5)], 18)
print(element_find([-1, -2, 0, 8, 5, 7, 9], 8))                    # ([(-1, 9), (0, 8)], 6)
print(element_find([-1, -2, 0, 8, 5, 7, 9], 10))                   # None
print(element_find([2], 10))                                       # None
print(element_find([1, 5, 2, 7, 4, 9], 11))                        # ([(2, 9), (4, 7)], 8)
