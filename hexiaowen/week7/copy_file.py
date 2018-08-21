from pathlib import Path
import shutil


def copy_file(path,copy_path):
    path = Path(path)
    if path.is_file():                              #判断是否为文件
        file_name = path.name
    copy_path += file_name                          #设置新路径
    copy_path = Path(copy_path)
    shutil.copyfileobj(f1,f2)                       #复制文件

copy_file('F:/python程序/第7周/作业/test.txt','F:/python程序/第7周/作业/test/')