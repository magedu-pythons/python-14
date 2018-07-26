a = 0              #方法一
b = 1
print(0)
print(1)
i = 1
while i <101:
    sum = a + b
    print(sum)
    a =b
    b = sum
    i += 1


    
def FIbo(n):           #方法二
    if n == 0 or n ==1 :
        return(1)
    else:
        sum = FIbo(n-1)+FIbo(n-2)
        return sum
for i in range(0,101):
    print(FIbo(i))


