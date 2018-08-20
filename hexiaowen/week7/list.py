li = [ [ ] ] * 5
print(li)
print(id(li[0]),id(li[1]))
# li[0].append(10)
# print(li)
# li[1].append(20)
# print(li)
# li.append(30)
# print(li)
'''
[ [] ]*5 是将内层列表复制五次，指向同一个对象，
由程序可以看出每一个列表的id都是一样的
'''