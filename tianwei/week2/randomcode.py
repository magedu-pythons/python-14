#实现随机生成 200 无重复激活码（或者优惠券），字符串长度大于5以上

import random

str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'

codelist = []
count=0
while count<200:
    code = ''
    for i in range(5):
        code += random.choice(str)
    if code not in codelist:
        codelist.append(code)
        count+=1

print(codelist)


