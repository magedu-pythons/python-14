l = []
max1 = max2 = max3 = 0
for i in range(20):
    l.append(random.randint(1,100))

print(l)
max1 = max(l)
l.remove(max1)
max2 = max(l)
l.remove(max2)
max3 = max(l)

print('最大的数:{},第二大的数:{},第三大的数:{}'.format(max1,max2,max3))