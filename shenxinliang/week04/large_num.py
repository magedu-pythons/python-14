import random
lst = [random.randint(1, 50) for i in range(20)]   #随机生成20个整数的列表
print("随机生成20个数：\n",lst)
lst.sort()                                         #调用sort函对lst列表升序排序
print("排序筛选出最大的3个数：\n",lst[-1],lst[-2],lst[-3])  #在排好序的列表中，找出最后3个数字即最大的三个