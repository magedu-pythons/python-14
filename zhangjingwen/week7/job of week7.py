# 1、请将 "1,2,3"，变成 ["1","2","3"]
print("1,2,3".split(","))
print([x for x in "1,2,3".replace(',', '')])
print([x for x in filter(lambda i:not","in i, "1,2,3")])
print([x for x in "1,2,3"[::2]])

# 2、使用Python copy一个文件，从a目录,copy文件到b目录
from pathlib import Path
import shutil
import os


p1 = Path("F:/python-14/zhangjingwen/week7/a/test.txt")
p2 = Path("F:/python-14/zhangjingwen/week7/b")
if p1.exists():
    if not p2.exists():
        p2.mkdir(parents=True)
    shutil.copy2(str(p1), str(p2))
else:
    print("Source path not exist!")
print(os.stat(str(p1)))
print(os.stat(str(p2)+'/test.txt'))


# 3、以下代码输出什么，请解释原因(写到问题下方):
li = [ [ ] ] * 5
li[0].append(10)
print(li)
"""
输出：[[10],[10],[10],[10],[10]]
原因：[ [ ] ] * 5本质是调用了浅拷贝，在遇到可变类型时仅复制了一个引用，即li[1]到li[4]都同时指向li[0]对应的内存地址
，li[0]发生改变时，li[1]等也会相应地随之改变。
"""
li[1].append(20)
print(li)
"""
输出： [[10，20],[10，20],[10，20],[10，20],[10，20]]
原因同上，改变li[1]与改变li[0]有同样的效果
"""
li.append(30)
print(li)
"""
输出： [[10，20],[10，20],[10，20],[10，20],[10，20],30]
原因： 改变的是li对象的值，不涉及引用类型
"""