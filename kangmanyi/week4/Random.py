#随机生成20个数字，并且筛选出其中最大的3个数
import random

numbers = []
for i in range(20):
    numbers.append(random.randint(-100,100))
print(numbers)
lst = numbers
lst.sort(reverse=True)
print(lst[:3])