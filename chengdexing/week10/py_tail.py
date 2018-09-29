# 2、实现一个函数获取一个目录下所有以.py结尾的文件（包含目录下的子目录中的.py文件）


from pathlib import Path
file_list = []


def file_is(item):
    if item.suffix == '.py':
        file_list.append(item.name)


def dir_is(p):
    for item in p.iterdir():
        if item.is_dir():
            dir_is(item)
        elif item.is_file():
            file_is(item)


def tail(path: str):
    global file_list
    p = Path(path)
    if p.exists():
        if p.is_dir():
            dir_is(p)
        elif p.is_file():
            file_is(p)
    else:
        return


tail(r'F:\python\workspace')
print(file_list, len(file_list))



