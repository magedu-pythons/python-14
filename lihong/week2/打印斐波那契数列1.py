#打印斐波那契数列
#Method one
num1=0
num2=1
print(num2)
for _ in range(100):
    num3=num1+num2
    num1=num2
    num2=num3
    if num3<100:
        print(num3)
