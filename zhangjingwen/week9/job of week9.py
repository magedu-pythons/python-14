"""1、请实现函数 new_counter ，使得调用结果如下：
      c1 = new_counter(10)
      c2 = new_counter(20)
      print（c1(), c2(), c1(), c2()）
      outputs ：
      11 21 12 22
"""


def new_counter(num: int):
    def fn():
        nonlocal num
        num += 1
        return num
    return fn


c1 = new_counter(10)
c2 = new_counter(20)
print(c1(), c2(), c1(), c2())           # 11 21 12 22

# ----------------------------------------------------------------------------
# 2、实现一个函数，输入字符串，判断该字符串是否不含有重复字符
'''思路：遍历字符串，将各个元素出现次数记录于字典中，取出仅出现一次的元素'''

import re
from collections import defaultdict


def string_check(src: str, ignore_case=True, only_alpha=True):
    regex = re.compile('[a-zA-Z]+') if only_alpha else re.compile('.+')
    new = ''.join(regex.findall(src))

    record = defaultdict(lambda: 0)
    new = new.lower() if ignore_case else new
    for x in new:
        record[x] += 1
    single = [k for k, v in record.items() if v == 1]

    return single if single else False


"""test"""
print(string_check('aabb'))                         # False
print(string_check('aabbc'))                        # ['c']
# 是否忽略大小写
print(string_check('AaBbCc'))                       # False
print(string_check('AaBbCc', ignore_case=False))    # ['A', 'a', 'B', 'b', 'C', 'c']
# 是否仅核对字母
print(string_check('ab12@*'))                       # ['a', 'b']
print(string_check('abb12@*', only_alpha=False))    # ['a', '1', '2', '@', '*']
# 核对所有字符、不忽略大小写
print(string_check('Aa12@*', ignore_case=False, only_alpha=False))   # ['A', 'a', '1', '2', '@', '*']