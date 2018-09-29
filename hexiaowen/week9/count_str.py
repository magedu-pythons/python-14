def count_str(str1):
    '''
    实现一个函数，输入字符串，判断该字符串是否不含有重复字符
    '''
    set1 = set(str1)
    print('no duplicate string') if len(str1) == len(set1) else print('have duplicate string')

count_str('123')