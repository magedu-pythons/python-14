import os


def Find_Py(path, flag=''):
    fileslst = os.listdir(path)
    flag += '>'
    for fileName in fileslst:
        nextpath = os.path.join(path, fileName)
        if os.path.isdir(nextpath):
            print("{}子目录:{}".format(flag, nextpath))
            Find_Py(nextpath, flag)
        elif fileName.endswith('.py'):
            print(flag, fileName)


path = r"files"
print("目录:{}".format(path))
Find_Py(path)
