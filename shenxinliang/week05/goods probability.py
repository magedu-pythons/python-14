#已知仓库中有若干商品，以及相应库存，类似：袜子，10 鞋子，20 拖鞋，30 项链，40
#要求随机返回一种商品，要求商品被返回的概率与其库存成正比。请描述实现的思路或者直接写一个实现的函数

import random

Wa_Zhi     = ['WZ'] * 100
Xie_Zi     = ['XZ'] * 200
Tuo_Xie    = ['TX'] * 300
Xiang_Lian = ['XL'] * 400

All_Before = Wa_Zhi + Xie_Zi + Tuo_Xie + Xiang_Lian  #All_Before是按1:2:3:4 的比率的货物列表，方便统计各货物是原来的100倍
All_After  = random.sample(All_Before, 100)   # 从All_Before中随机获取100个元素,组成100次取货记录

print ("取100次货物的概率")                   # 统计100次取货记录，满足1:2:3:4的货物比率
print ("袜子的概率：",All_After.count('WZ'))
print ("鞋子的概率：",All_After.count('XZ'))
print ("拖鞋的概率：",All_After.count('TX'))
print ("项链的概率：",All_After.count('XL'))