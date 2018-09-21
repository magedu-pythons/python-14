'''
给出一个无序的整型列表，找出最长连续元素序列的长度，时间复杂度要求在线性时间内。
例如：
    输入：[8, 1, 9, 3, 2, 4 ]，那么其最长连续序列是[1, 2, 3, 4]，即输出长度为4
'''


def longlst(lst):
    log = 0
    sets = set(lst)
    for v in lst:
        logslst = [v]
        valadd = valsub = v
        length = 1
        for _ in range(len(sets)):
            if valsub - 1 in sets:
                length += 1
                valsub -= 1
                logslst.append(valsub)
                sets.remove(valsub)
            if valadd + 1 in sets:
                length += 1
                valadd += 1
                logslst.append(valadd)
                sets.remove(valadd)
        if length > log:
            log = length
            loglst = logslst
            loglst.sort()
    print("最长连续序列是{}，即输出长度为{}".format(loglst, log))


lst = [8, 3, 1, 9, 4, 2]
longlst(lst)
