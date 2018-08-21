#使用Python copy一个文件，从a目录,copy文件到b目录

import shutil

shutil.copyfile('D:\PythonProjects\mypython\CopyFile.py','E:\GitHub\python-14\\tianwei\week7\CopyFile.py')

#在python中\是转义字符，\tianwei中，\t是制表字符，要想正常使用路径需要改成如下形式\\tianwei,或者直接用斜杠/不用反斜杠\