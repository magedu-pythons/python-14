#一个5位数，判断它是不是回文数
num = input("please enter a five-digit number: ")
flag=True
for i in range(2):
    if num[i]!=num[-i-1]:
        print("不是回文数")
        break
else:
    print("是回文数")
