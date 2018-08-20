#使用Python copy一个文件，从a目录,copy文件到b目录
import shutil

f1 = open('E:/Github/python-14/shenxinliang/week07/a/1.txt','r+')  # a 目录文件

f2 = open('E:/Github/python-14/shenxinliang/week07/b/2.txt','w+')  # b 目录拷贝文件

shutil.copyfileobj(f1,f2)   #shutil.copyfileobj(文件1，文件2)：将文件1的数据覆盖copy给文件2