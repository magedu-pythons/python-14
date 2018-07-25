#!/usr/bin/env python
#.Author:Dyw
#-*- coding:utf-8 -*-
import random,string
num=string.digits
nums = []
for i in range(20):
    nums.append(random.choice(num))
nums.sort(reverse=True)
print(nums)
print('The first three largest numbers is:',nums[0],nums[1],nums[2])