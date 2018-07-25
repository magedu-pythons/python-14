# 2、随机生成20个数字，并且筛选出其中最大的3个数
import random


sign = ['+','-']
ratio = [10**i for i in range(9)]

nums = []
for _ in range(20):
    base = [random.random(), random.randint(1, 10)]
    num = random.choice(sign) + str(random.choice(base) * random.choice(ratio))
    if '.' in num:
        nums.append(float(num))
    else:
        nums.append(int(num))
nums.sort()
print('All nums are:\n{}'.format(nums))
print("The first three largest Numbers are:\n{}".format(nums[-1:-4:-1]))


#运行结果
'''
All nums are:
[-90000000, -7000000, -2000000, -90000, -40000, -40000, -9697.759659600048, -5184.420125416943, -396.59179990056913, -30, 
0.21107941608713077,30, 397.0061521800744, 8000, 600000, 1471733.6890839273, 2000000, 6000000, 29134860.10755708, 52425969.68838277]

The first three largest Numbers are:
[52425969.68838277, 29134860.10755708, 6000000]
'''
