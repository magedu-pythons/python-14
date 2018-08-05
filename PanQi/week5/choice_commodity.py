list = []
Warehouse = {'Socks':10,'Shoes':20,'Slipper':30,'Necklace':40}
for k,v in Warehouse.items():
    pro = 0
    pro = v //10
    for i in range(pro):
        list.append(k) 
print (list)   

for j in range(10): #假设查询10次
     print (random.choice(list))  #从列表中随机取一个
    # random.shuffle(list)        #先把列表打乱
    # print (list[0])             #每次取任意一个都行
