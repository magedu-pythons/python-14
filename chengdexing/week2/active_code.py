#生成随机激活码
import random

lst_code = []
active_code = ''
value = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
for n in range(50):
    num = 0
    for i in range(25):
        num += 1
        active_code += random.choice(value)
        if num % 5 == 0 and num != 25:
            active_code += '-'
    lst_code.append(active_code)
    active_code = ''
set(lst_code)

for i in lst_code:
    print(i)




