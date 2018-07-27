num = input('请输入一个5位数：')

if num[0] == num[4] and num[1] == num[3]:
    print('{}是回文数'.format(num))
else:
    print('{}不是回文数'.format(num))
