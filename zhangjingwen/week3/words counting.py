# 要求：任一个英文的纯文本文件，统计其中的单词出现的个数。
from collections import OrderedDict


def wordsCount(file):
    with open(file,'r') as f:
        base = f.read()
    words = base.lower().split()

    record = {}                   #统计单词出现频次
    for x in words:
        x = x.strip('.').strip(',')
        count = record.setdefault(x,0)
        count += 1
        record[x] = count

    length = len(record)          #用嵌套列表将单词按照出现频次归类
    wordsOrder = [[] for _ in range(length)]
    for k,v in record.items():
        wordsOrder[v].append(k)

    repeat = OrderedDict()        #用顺序字典按照降序重新记录单词出现频次
    for i in range(length-1,0,-1):
        if wordsOrder[i]:
            for j in range(len(wordsOrder[i])):
                repeat[wordsOrder[i][j]] = i

    for key in repeat:            #按出现频次降序打印
        print("the word {:^10} repeated  {:^4} times".format(key,repeat.get(key)))


wordsCount('F:\\python-14\\zhangjingwen\\week3\\a song of ice and fire.txt')

#输出效果：
# the word    the     repeated   79  times
# the word    and     repeated   49  times
# the word     of     repeated   34  times
# the word     a      repeated   30  times
# the word    his     repeated   22  times
# the word    was     repeated   17  times
# the word     as     repeated   17  times
# the word     he     repeated   14  times
# the word     in     repeated   13  times
# the word     to     repeated   12  times

