import collections
import random

#方法一
# def percentage():    #返回一个商品
#     goods_dict = {'项链':40,'拖鞋':30,'鞋子':20,'袜子':10}
#     count_dict = collections.OrderedDict()
#     count = 0
#     for k,v in goods_dict.items():               #统计商品数值范围，做一个有序列表
#         count += v
#         count_dict[k] = count
#     number = random.randint(1,count)             #生成一个随机数
#     for k,v in count_dict.items():               #判断随机数的范围，返回一个商品
#         if number <= v:
#             return k

#方法二
def percentage():
    lst = ['项链', '拖鞋', '鞋子', '袜子']
    goods_dict = {'项链': 0, '拖鞋': 0, '鞋子': 0, '袜子': 0}
    good = random.choices(lst, weights=[40, 30, 20, 10])
    return good[0]

def count_good(n):            #计算percentage()程序返回商品的概率
    count_dict = {}
    for _ in range(n):
        goods = percentage()
        if goods not in count_dict.keys():
            count_dict[goods] = 1
        else:
            count_dict[goods] += 1
        #count_dict[goods] = count_dict[goods] + 1 if goods in count_dict.keys() else 1
    for k,v in count_dict.items():
        count_dict[k]=v/n
    print(count_dict)

#print(percentage())
count_good(10000)