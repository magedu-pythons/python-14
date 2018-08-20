# 1、实现一个函数用于判断字符串str2是否是str1的子串。如果是，则该函数返回str2在str1中首次出现的地址；否则，返回None。

# 方法一 将子串代入源字符串中逐一对比，仿照find()的功能
def finder(src: str, sub: str, start=0, end=-1):
    """
    功能：仿字符串的find()方法
    :param src: source string,user provide
    :param sub: the substring,user provide
    :param start: the start index of the src string
    :param end: the end index of the src string and the element it points to is contained
    :return: tuple or None
    """
    if len(src) >= len(sub) > 0 and bool(src[start:end]):
        _end = end if end >= 0 else end+len(src)
        _start = start if start >= 0 else start+len(src)   # 负索引转成正索引处理
        _src = src[_start:_end+1]

        ''' 递归判断子串与源是否存在匹配'''
        def match(_src, sub, sub_index=0, _src_index=0, match_count=0):
            while _src_index < len(_src):
                if sub[sub_index] == _src[_src_index]:  # 首字符匹配则源和子串的索引号+1，递归比较后续字符是否匹配
                    sub_index += 1
                    _src_index += 1
                    match_count += 1
                    if sub_index < len(sub):
                        return match(_src, sub, sub_index, _src_index, match_count)
                    else:
                        return (_src_index-len(sub)+start, _src_index+start)
                else:                                   # 匹配失败，子串索引回到0，继续在源中向后寻找匹配
                    sub_index = 0
                    _src_index = _src_index-match_count+1
                    match_count = 0
                    return match(_src, sub, sub_index, _src_index, match_count)
            else:
                return
        return match(_src, sub)
    else:
        return


"""TEST
不存在时返回None；存在时返回元组，使用元组元素对原字符串切片即为目标子串"""
print(finder('aabbcc', 'dd'))           # None
print(finder('aabbcc', ''))             # None
print(finder('aabbcc', 'bb'))           # (2, 4)
print(finder('aabbcc', 'bb', 2, 3))     # (2, 4)
print(finder('aabbcc', 'bb', end=-5))    # None
print(finder('aabbcc', 'b'))            # (2, 3)
print(finder('aabbcc', 'aabbcc'))       # (0, 6)


# ------------------------------------------分割线--------------------------------------------------------
# 方法二 以sub为分隔符切割源字符串
def finder(src, sub, start=0, end=-1):

    if len(src) >= len(sub) > 0 and bool(src[start:end]):
        _end = end if end >= 0 else end + len(src)
        _start = start if start >= 0 else start + len(src)  # 负索引转成正索引处理
        _src = src[_start:_end + 1]

        if sub in _src:
            dest = _src.split(sub)
            return (len(dest[0])+start, len(dest[0])+len(sub)+start)
        else:
            return
    else:
        return


"""TEST
不存在时返回None；存在时返回元组，使用元组元素对原字符串切片可得到目标子串"""
print(finder('aabbcc', 'dd'))           # None
print(finder('aabbcc', ''))             # None
print(finder('aabbcc', 'bb'))           # (2, 4)
print(finder('aabbcc', 'bb', 2, 3))     # (2, 4)
print(finder('aabbcc', 'bb', end=-5))    # None
print(finder('aabbcc', 'b'))            # (2, 3)
print(finder('aabbcc', 'aabbcc'))       # (0, 6)

