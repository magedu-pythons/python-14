#无重复字符的最长子串
#给定 "abcabcbb" ，没有重复字符的最长子串是 "abc" ，那么长度就是3。
#给定 "bbbbb" ，最长的子串就是 "b" ，长度是1。
#给定 "pwwkew" ，最长子串是 "wke" ，长度是3。请注意答案必须是一个子串，"pwke" 是 子序列  而不是子串。

s1="abcabcbb"
s2="bbbbb"
s3="pwwkew"
s4='au'
s5=" "
s6='abbbbba'
def longestsub(str):
    maxsubstr = ''
    maxn = 0
    if len(str)==1:
        maxsubstr=str
        maxn=1
    else:
        for i in range(len(str)):
            temstr = str[i]
            for j in range(i + 1, len(str)):
                if str[j] not in temstr:
                    temstr+=str[j]
                else:
                    break
            if len(temstr) > maxn:
                    maxn=len(temstr)
                    maxsubstr=temstr

    return maxsubstr,maxn

print(longestsub(s1))

