# 2、使用Python copy一个文件，从a目录,copy文件到b目录
import shutil

try:
    shutil.copyfile(r'e:/a/a.txt', r'e:/b/b.txt')
    print('copy accomplish!')
except Exception as e:
    print('copy failure!')
