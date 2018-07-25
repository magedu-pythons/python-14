# 2、随机生成20个数字，并且筛选出其中最大的3个数
import random


sign = ['+','-']
ratio = [10**i for i in range(9)]

nums = []
for _ in range(20):
    base = [random.random()*random.choice(ratio), int(random.random()* random.choice(ratio))]
    num = random.choice(sign) + str(random.choice(base))
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
[-9458189.376565212, -121550, -64123, -4759.4901779010415, -776.4226404972998, -360.33377511583564, -35.95861884751383, -26.705539025014502, -1.081408343478456, 
-0.6265000803522942,-0.6089768366254978, -0.4224645927591364, -0.3240733791802193, 0.08910083275222247, 0.5640521846126217, 8, 65, 69, 98923, 2223219.7626520954]

The first three largest Numbers are:
[2223219.7626520954, 98923, 69]
'''
