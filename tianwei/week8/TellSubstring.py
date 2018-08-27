#实现一个函数用于判断字符串str2是否是str1的子串。如果是，则该函数返回str2在str1中首次出 现的地址；否则，返回None。

def TellSubstr(str1:str,str2:str):
    for i in range(len(str1)):
        if str2==str1[i:i+len(str2)]:
            return i
    else:
        return None

s1='ddabcabbb'
s2='ab'
print(TellSubstr(s1,s2))