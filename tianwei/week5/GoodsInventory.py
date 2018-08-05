#已知仓库中有若干商品，以及相应库存，类似：袜子，10 鞋子，20 拖鞋，30 项链，40
#要求随机返回一种商品，要求商品被返回的概率与其库存成正比。请描述实现的思路或者直接写一个实现的函数
import random

def goods():
    goods = ["socks", "shoes", "slippers", "necklaces"]
    po = [0.1, 0.2, 0.3, 0.4]
    p=random.random()
    pop = 0
    for i in range(4):
        pop+=po[i]
        if p< pop:
            return goods[i]

print(goods())
