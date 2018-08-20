# 2、给定一个整型列表，请实现从其中找出2个数的和为某一个指定的值？
# 如：lst =[1,5,2,7,4,9]，指定的目标值为11，可以从中找出 2和9之和为11
"""思路：利用中值折半，减少遍历次数"""


def element_find(src: list, num: int):
    average = num/2
    new = src.copy()
    while len(src) >= 2:
        new.append(average)
        new.sort()
        index = new.index(average)

        result = []
        for i in range(index):
            for j in range(index+1, len(new)):
                if new[i]+new[j] == num:
                    result.append((new[i], new[j]))
        return result if result else None
    else:
        return


'''test'''
print(element_find([-1, -2, 0, 8, 5, 7, 9], 8))     # [(-1, 9), (0, 8)]
print(element_find([-1, -2, 0, 8, 5, 7, 9], 10))    # None
print(element_find([2], 10))                        # None
print(element_find([1, 5, 2, 7, 4, 9], 11))         # [(2, 9), (4, 7)]