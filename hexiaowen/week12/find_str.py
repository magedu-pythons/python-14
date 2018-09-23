'''
3、输入一个字符串，求不含有重复字母的最长子串的长度
例如：
   输入字符串'aaa'，其不含有重复字母的最长子串为‘a’，输出长度为1
'''
str1 = 'abcaabdcdabcd'

def x(str):
    result = []
    max_length = [0]
    flag = [0]
    for i in range(len(str)):
        dict = {}
        length = 0
        for j in range(i,len(str)):
            dict[str[j]] = dict.get(str[j],0) +1
            if dict[str[j]] == 2:
                break
            elif dict[str[j]] == 1:
                length += 1
            if length > max_length[0]:
                max_length = [length]
                flag = [i]
            elif length == max_length[0]:
                max_length.append(length)
                flag.append(i)
    if max_length[0] == i-len(str)+1:
        for x in range(len(flag)):
            result.append(str[flag[x]:flag[x]+max_length[x]])
        return result
    for x in range(len(flag)):
        result.append(str[flag[x]:flag[x] + max_length[x]])
    return result

print(x(str1))