'''
输入一个字符串，求不含有重复字母的最长子串的长度
例如：
    输入字符串'aaa'，其不含有重复字母的最长子串为'a',输出长度为1
'''
import re


def deal_str(strs):
    prev = 0
    lens = len(strs)
    while prev < lens:
        strl = strs[0:prev+1]
        if re.findall(r'[a-zA-Z]+', strs[prev:prev+1]):
            strr = strs[prev:].replace(strs[prev].lower(), "")
            strr = strr.replace(strs[prev].upper(), "")
            strs = strl + strr
        prev += 1
    print("最长子串：{}，长度={}".format(strs, len(strs)))


deal_str(str(input("请输入一个字符串：")))  # 测试：'afbAc1 acMb2 ced3 bcFe4 acDe5 vvd6 bmc'

