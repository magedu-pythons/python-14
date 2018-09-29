#实现一个函数获取一个目录下所有以.py结尾的文件（包含目录下的子目录中的.py文件）

from pathlib import Path

def getpyfile(str):
    path=Path(str)
    filepath=path.glob('**/*.py')
    lst=[]
    for i in filepath:
        lst.append(i.name)
    print(lst)



getpyfile('D:\PythonProjects\mypython\homework')