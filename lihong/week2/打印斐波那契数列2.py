#打印斐波那契数列
#Method two
num1=0
num2=1
while True:
    num1,num2=num2,num1+num2
    print(num1)
    if num2>100:
        break