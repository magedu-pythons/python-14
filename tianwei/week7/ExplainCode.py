#以下代码输出什么，请解释原因(写到问题下方):

li = [ [ ] ] * 5   #list浅拷贝，复制的元素都是第一个[]的地址
li[0].append(10)
print(li)         #原始空列表追加元素后，其他复制原始空列表地址的元素也更改

print("*"*20)

li[1].append(20)     #都是同一个地址
print(li)

print("*"*20)

li.append(30)        #li列表末尾增加元素30
print(li)