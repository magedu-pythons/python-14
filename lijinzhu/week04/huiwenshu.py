#!/usr/bin/env python
#author: Li Jinzhu
#Blog: http://blog.51cto.com/limingyu

while True:
    num = input("请输入一个5位数： ")
    
    if num.isdigit():
        num = int(num)
        if num > 9999 and num < 100000:
            a = num % 10 #个
            b = num % 100 // 10 #十
            x = num % 10000 // 1000 #千
            y = num // 10000 #万
            if a == y and b == x:
                print("{} is a hui wen shu".format(num))
                break
            else:
                print("{} is not a hui wen shu".format(num))
        else:
            print("您输入的不是五位数，请重新输入： ")
    else:
        print("Error,您输入的不是数字，请重新输入:  ")

