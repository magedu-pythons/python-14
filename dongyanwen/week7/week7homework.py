#!/usr/bin/env python
#.Author:Dyw

#01、请将 "1,2,3"，变成 ["1","2","3"]
lst="1,2,3"
print(lst.split(','))


#02、使用Python copy一个文件，从a目录,copy文件到b目录
import shutil
with open('sample.txt','r+') as f1:
    with open('/tmp/sample.txt.bak','w+') as f2:
        shutil.copyfileobj(f1,f2)


#03、以下代码输出什么，请解释原因(写到问题下方):
li = [ [ ] ] * 5
li[0].append(10)
print(li)
li[1].append(20)
print(li)
li.append(30)
print(li)
#输出：
[[10], [10], [10], [10], [10]]
[[10, 20], [10, 20], [10, 20], [10, 20], [10, 20]]
[[10, 20], [10, 20], [10, 20], [10, 20], [10, 20], 30]
#解答：
"""
In [40]: id(li)
Out[40]: 140303643516424

In [41]: id(li[0])
Out[41]: 140303675547720

In [42]: id(li[1])
Out[42]: 140303675547720
因为li所有的元素id都是一样的，所以如果修改一个元素，
其余的元素也会跟之修改，但是li本身的id不同于它的元素，
所以li.append(30)只会在最后追加元素
"""