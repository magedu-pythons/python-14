import random
a=[1,2,3,4,5,6,7,8,9,0,"A","B","C","D","E","F","G","H","J",]
for i in range (0,200):
    c=[]
    for j in range (0,5):
        b=random.choice(a)
        c.append(b)
    print (c)   #怎么转换成字符串啊，试了用join函数，没成功

