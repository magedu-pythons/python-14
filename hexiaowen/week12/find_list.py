'''
2、给出一个无序的整型列表，找出最长连续元素序列的长度，时间复杂度要求在线性时间内。
例如：
    输入：[8,1,9,3,2,4]，那么其最长连续序列是[1,2,3,4]，即输出长度为4
'''
list = [4,5,4,1,2,2,3,7,8]
max_num = max(list)
list_count = [0] * max_num
for i in list:
    list_count[i-1] = i

def k(list_count):
    max_flag = 0
    max_length = 0
    length = 0
    for i in range(len(list_count)):
        if list_count[i] != 0:
            length += 1
        elif list_count[i] == 0:
            if max_length < length:
                max_length = length
                max_flag = i
            length = 0
    return list_count[max_flag-max_length:max_flag]

print(k(list_count))