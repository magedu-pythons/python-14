#100以内斐波那契数列
#方法一
i, j = 1, 1
while i < 100:
    print (i)
    i, j = j, i+j

#方法二
list = [1,1]
for i in range(100):
   f = list[1] + list[i+1]
   list.append(f)