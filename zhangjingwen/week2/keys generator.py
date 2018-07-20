# 要求：使用 Python 实现随机生成 200 无重复激活码（或者优惠券），字符串长度大于5以上

import random

def productKey(length,nums=200):
    key = []
    base = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    while len(key)<nums:
        s1 = ''
        for _ in range(length):
            s1 += random.choice(base)
        key.append(s1)
        key = list(set(key))
    print('\n'.join(key))

productKey(*[12,200])


