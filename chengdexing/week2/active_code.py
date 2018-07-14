#生成随机激活码
import random

lst_code = []
active_code = ''
value = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
num = 0
for n in range(50):
    for i in range(25):
        num += 1
        active_code += random.choice(value)
        if num % 5 == 0 and num != 25:
            active_code += '-'
    num = 0
    lst_code.append(active_code)
    active_code = ''

for i in lst_code:
    print(i)




