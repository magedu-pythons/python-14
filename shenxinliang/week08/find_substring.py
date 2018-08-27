#实现一个函数用于判断字符串str2是否是str1的子串。如果是，则该函数返回str2在str1中首次出现的地址；否则，返回None


def find_str(str_1,str_2):
    result = str_2.split(str_1)  #以str_1的字符作为str_2的分割
    if len(result) == 0:
        return None
    if result[0] == '':
        return 0
    else:
        return len(result[0])
str_1 = "i"
str_2 = "this is test word  "
print (str_2,str_1)
print(find_str(str_1,str_2))