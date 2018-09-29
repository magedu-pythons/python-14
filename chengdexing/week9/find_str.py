# 2、实现一个函数，输入字符串，判断该字符串是否不含有重复字符

word = """ajfdkjfkweirdfkdfer"""


def repe_str(iterable):
    for item in word:
        if word.count(item) >= 2:
            print('有重复字符')
            break
    else:
        print('没有重复字符')

repe_str(word)


