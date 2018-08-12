#一个5位数，判断它是不是回文数。
num = input("请输入任意一个数")
if num == num[::-1]:
    print('%s is a palindrome number'% num)
else:
    print('%s is not a palindrome number'% num)
