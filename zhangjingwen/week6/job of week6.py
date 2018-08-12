# 现有两元祖 (('a'),('b')),(('c'),('d')) ,请使用Python中的匿名函数生成列表 [ {'a':'c'｝,{'b':'d'}]

fn = lambda x, y: [{i: j for i in x[n] for j in y[n]} for n in range(len(x)) if len(x) == len(y)]

t1 = (('a'), ('b'))          # 元组的元素是字符串
t2 = (('c'), ('d'))
print(fn(t1, t2))            # [{'a': 'c'}, {'b': 'd'}]
print(type(fn(t1, t2)))      # class 'list'
print(type(fn(t1, t2)[1]))   # class 'dict'


fn = lambda x, y: [{i: j for i in x[n][0] for j in y[n][0]} for n in range(len(x)) if len(x) == len(y)]

t1 = (('a',), ('b',))        # 元组的元素类型是元组
t2 = (('c',), ('d',))
print(fn(t1, t2))            # [{'a': 'c'}, {'b': 'd'}]


# 输入一个英文句子,翻转句子中的单词顺序,但单词内字符的顺序不变
import re


def word_reverse(src: str):
    ignore_list = re.findall(r'[^A-Za-z ]+', src)
    print(ignore_list)
    for ignore in ignore_list:
        base = src.replace(ignore, ' ')
    new = base.split()
    new.reverse()
    yield from new


a = "well,i decided to be a computer programmer."
foo = word_reverse(a)
print(next(foo))
print(next(foo))
