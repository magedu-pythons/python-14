#给出任意一个列表，请查找出x元素是否在列表里面，如果存在返回1，不存在返回0
方法一：
lisa = [1,2,3,'a',[4,5,[6]],'b']
a = str(lisa)
flag = a.find(str(input('>>>')))
if flag != -1:
    print ('此数存在：1')
else:
    print ('此数不存在：-1')

方法二：
#交互式
a = None
lisa = []
while a != 'end':
    a = input('>>>')
    lisa.append(a)
a = str(lisa)
flag = a.find(str(input('>>>')))
if flag != -1:
    print ('此数存在：1')
else:
    print ('此数不存在：-1')
