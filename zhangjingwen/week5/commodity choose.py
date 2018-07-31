#1、打乱一个排好序的list对象alist，alist=[1,2,3,4,5]
import random


alist = [1,2,3,4,5]
random.shuffle(alist)

print(alist)


'''2、已知仓库中有若干商品，以及相应库存，类似：
袜子:10  鞋子:20  拖鞋:30  项链:40
要求随机返回一种商品，要求商品被返回的概率与其库存成正比。请描述实现的思路或者直接写一个实现的函数'''

import random


def commodityChoose(source:dict):
    if source:
        keys = [k for k in source.keys()]
        values = [source[i] for i in keys]
        goods = random.choices(keys,values,k=1)
        return goods[0]+' the probability is {}%'.format(source[goods[0]]/sum(values)*100)
    return

d = {}
d1 = {'袜子':10,'鞋子':20,'拖鞋':30,'项链':40}
print(commodityChoose(d1))