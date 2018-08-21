#  1.请将"1,2,3",变成["1", "2","3"]
import re

str_bf = '"1,2,3"'
print(str_bf)
lst_end = re.findall(r'[^,"]+', str_bf)
print(lst_end)


# 2.使用Python copy一个文件，从a目录，copy文件到b目录"
import shutil

with open('a/test.txt', 'r+') as f1:
    with open('b/test.txt', 'w+') as f2:
        shutil.copyfileobj(f1, f2)

# 3.以下代码输出什么，请解释原因（写到问题下方）：
print("代码输出：")
li = [[]]*5
li[0].append(10)
print(li)
li[1].append(20)
print(li)
li.append(30)
print(li)

print("原因：")
print("1.列表li生成后为[[],[],[],[],[]]，5个元素li[0]…li[4]都引用了[]所在的内存空间，被分配了相同的内存地址；\n"
      "2.当li[0]…li[4]中任何一个要修改值时，相当于指向[]的内存地址，然后对[]内存空间中的值进行修改，相应的li[0]…li[4]都引用[]内存空间中的值；\n"
      "3.li.append(30)是给列表li添加新的一个元素，会给这个元素分配新的内存空间和地址，所以只会影响它本身，对其他的元素不产生影响；")

