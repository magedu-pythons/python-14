# 2、两个有序数组，分别拥有m和n的长度，求其合并后的第k个值

def merge(lst1, lst2, k: int):
    m = len(lst1)
    n = len(lst2)
    lst1 += [0] * n

    if m > 0 and n == 0:
        res = lst1
    elif n > 0 and m == 0:
        res = lst2
    elif m > 0 and n > 0:
        while m > 0 and n > 0:
            if lst1[m-1] >= lst2[n-1]:
                lst1[m+n-1] = lst1[m-1]
                m -= 1
            else:
                lst1[m+n-1] = lst2[n-1]
                n -= 1
        if n > 0:
            lst1[:n] = lst2[:n]
        res = lst1
    else:
        res = []

    try:
        out = res[k]
    except IndexError:
        out = None
    finally:
        return out

print(merge([1, 2, 3], [4, 5, 6, 7], 4))        # 5
print(merge([], [], 4))                         # None
print(merge([1, 1], [], 1))                     # 1
print(merge([1, 2], [3], 2))                    # 3

