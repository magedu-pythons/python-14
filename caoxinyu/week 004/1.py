num = input('请输入一个五位数').strip
if len(num) != 5:
    print('请重新输入！')
if num[0] == num[-1] and num[1] == num[-2]:
    print('该数是回文数')
else:
    print('该数不是回文数')

