# 3、以下代码输出什么，请解释原因(写到问题下方):

li = [[]] * 5
print(id(li))


# 测试代码
#for i in range(5):
#    print('li{} id={}'.format(i, id(li[0])))
#print()

li[0].append(10)
print(li)

li[1].append(20)
print(li)

li.append(30)
print(li)


'''
    因为列表是可变类型，当对列表元素进行修改时列表中的
元素地址都没有改变所以用append方法追加元素时因为都是相
同地址所以对所有的元素都进行了改变
'''

