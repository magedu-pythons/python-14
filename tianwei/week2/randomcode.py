#实现随机生成 200 无重复激活码（或者优惠券），字符串长度大于5以上

import random

str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
length = len(str)

for x in range(200):
    code = ''
    for i in range(5):
        code += random.choice(str)
    print(code)


