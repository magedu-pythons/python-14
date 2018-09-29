# 1、实现一个可迭代的类
class Fib:
    def __init__(self, n):
        self.item = [1, 1]
        self.cal(n)

    def __str__(self):
        return str(self.value)

    def iter(self):
            yield from self.item

    def getitem(self, index):
        try:
            value = self.item[index]
        except IndexError:
            return None
        else:
            return value

    def cal(self, num):
        if num >= 2:
            for i in range(2, num):
                self.item.append(self.item[i-2] + self.item[i-1])
        else:
            return


# f = Fib(4)              # fib数列的前n项
#
# print(f.getitem(4))     # None
#
# for x in f.iter():
#     print(x, end=' ')   # 1 1 2 3


# 2、给出一个无序的整型列表，找出最长连续元素序列的长度，时间复杂度要求在线性时间内。
# 例如：
#     输入：[8,1,9,3,2,4]，那么其最长连续序列是[1,2,3,4]，即输出长度为4
def Linked_int(lst):
    record = {}

    for x in lst:
        if x not in record:
            if x - 1 in record and x + 1 in record:
                record[x] = record[x - 1] + record[x + 1] + [x]
                record[x - 1] = record[x]
                record[x + 1] = record[x]

            elif x-1 in record:
                record[x-1] += [x]
                record[x] = record[x-1]

            elif x+1 in record:
                record[x+1] += [x]
                record[x] = record[x+1]

            else:
                record[x] = [x]
    print(record)
    out = sorted(record, key=lambda x: len(record[x]), reverse=True)
    return len(record[out[0]])


print(Linked_int([8, 1, 9, 3, 2, 4]))               # 4
print(Linked_int([1, 1, 1, 1, 1]))                  # 1
print(Linked_int([1, 2, 3, 4, 5, 6, 7, 8, 9]))      # 9
print(Linked_int([1, 2, 3, 3, 4, 4, 5, 5, 6]))      # 6


# 3、输入一个字符串，求不含有重复字母的最长子串的长度
# 例如：
#    输入字符串'aaa'，其不含有重复字母的最长子串为‘a’，输出长度为1
def substr(src: str):
    if src:
        start_index = 0
        max_len = 0
        substr = {}

        for i, item in enumerate(src):
            index = substr.get(item)

            if index is not None and index >= start_index:
                start_index = index + 1
                max_len = max(max_len, i-start_index)
            else:
                max_len = max(max_len, i-start_index+1)

            substr[item] = i

        return max_len


print(substr('aaa'))        # 1
print(substr('abcdabc'))    # 4
print(substr('ababab'))     # 2
print(substr('eeeeeee'))    # 1
print(substr('aabbccdd'))   # 2
