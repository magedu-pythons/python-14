# 2、给定一个整型列表，请实现从其中找出2个数的和为某一个指定的值？
# 如：lst =[1,5,2,7,4,9]，指定的目标值为11，可以从中找出 2和9之和为11
"""思路：利用中值折半，减少遍历次数。"""


def element_find(src: list, num: int):
    new = src.copy()
    new.append(num/2)
    new.sort()
    index = new.index(num/2)
    same = [x for x in new[index+1:] if x == num/2]
    larger = [x for x in new[index+1:] if x > num/2]

    while len(src) >= 2:
        count1 = 0
        lst = []
        for i in range(index):
            for j in larger:
                count1 += 1
                if j > num-new[i]:
                    break                                         # 提前退出迭代
                if new[i] + j == num:
                    lst.append((new[i], j))
        # lst = [(new[i], j) for i in range(index) for j in larger if new[i] + j == num]

        if len(same) >= 2:                                        # 等于中值情况的处理
            for _ in range(len(same)-1):
                lst.append((same[0], same[0]))
        count = count1 + (len(same)-1 if len(same) >= 2 else 0)   # 迭代次数统计
        return (lst, count) if lst else None
    else:
        return


'''test'''
print(element_find([-1, -2, 0, 8, 5, 7, 9, 2, 5, 25, 14, 3], 8))    # ([(-1, 9), (0, 8), (3, 5), (3, 5)], 23)
print(element_find([-1, -2, 0, 8, 5, 7, 9], 8))                     # ([(-1, 9), (0, 8)], 12)
print(element_find([-1, -2, 0, 8, 5, 7, 9], 10))                    # None
print(element_find([2], 10))                                        # None
print(element_find([1, 5, 2, 7, 4, 9], 11))                         # ([(2, 9), (4, 7)], 7)
print(element_find([2, 2, 2, 2], 4))                                # ([(2, 2), (2, 2), (2, 2)], 3)

