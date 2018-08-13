teststr = 'abcda'

def f(str1):
    lenth = len(str1)
    if (lenth == 0) or (lenth == 1):
        return print('是')
    elif str1[0] == str1[-1]:
        str1 = str1[1:lenth-1]
        f(str1)
    elif str1[0] != str1[-1]:
        return print('否')

f(teststr)
