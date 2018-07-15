# 方法1：
i = 1
j = 1
t = 2
print (i,j,t,end=" ")
while True:
    i = j
    j = t
    t = int(i+j)
    if t > 100:
        break
    print (t,end=" ")

#方法2：
i = 1
j = 1
while i < 100:
    print (i,end=" ")
    i,j = j,i+j

