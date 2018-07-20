x=1
y=1
print(x,end=" ")
print(y,end=" ")
while(True):
    z=x+y
    x=y
    y=z
    if(z>100):    #通过z的临界条件决定数列打印范围
        break

    print(z,end=" ")

