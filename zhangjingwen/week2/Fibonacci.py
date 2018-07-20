#要求：打印出100以内的斐波那契数列，使用2种方法实现

# 方法一 按数列规律，求和后交换赋值
#print(1)
# cur = 1
# pre = 0
# while cur<=100:
#     sum = pre+cur
#     pre = cur
#     cur = sum
#     if cur>100: break
#     print(cur)

# 方法一变种
# print(1)
# pre = 0
# cur = 1
# while pre+cur<=100:
#     pre,cur = cur,pre+cur
#     print(cur)

# 方法二 将数列放在列表，利用列表索引并计算
l = [0,1]
i = 0
while l[-1]<=100:
    l.append(l[i]+l[i+1])
    print(l[i+1])
    i+=1

