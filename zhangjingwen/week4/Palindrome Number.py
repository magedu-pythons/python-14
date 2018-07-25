# 1、问题描述：一个5位数，判断它是不是回文数。
while True:
    num = input('>>>please input a number:').strip()
    if num.isdigit():
        break
    else: print('Invalid number,input again!')

for i in range(len(num)//2):
    flag = False
    if num[i] == num[len(num)-i-1]:
        flag = True
    else:
        print('No,the num {} is not a palindrome number.'.format(num))
        break
if flag:
    print('Yes,the num {} is a palindrome number.'.format(num))


# 运行效果
'''
>>>please input a number:454561516512
No,the num 454561516512 is not a palindrome number.

>>>please input a number:12345654321
Yes,the num 12345654321 is a palindrome number.

'''