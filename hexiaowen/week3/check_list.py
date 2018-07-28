list = input('请输入一个列表=')
code = input('请输入元素=')
for i in list:
    if code in i:
        print(1)
        break
else:
    print(0)