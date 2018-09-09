# 2、实现一个函数获取一个目录下所有以.py结尾的文件（包含目录下的子目录中的.py文件）
from pathlib import Path


def file_catch(path: str):
    def recursion_catch(p: Path):
        if not p.is_dir():
            return
        for file in p.iterdir():
            if file.is_dir():
                recursion_catch(file)
            elif file.is_file() and file.match('*.py'):
                file_list.append(str(file))

    file_list = []
    p = Path(path)
    if not p.exists():
        return
    if p.is_dir():
        recursion_catch(p)
    elif p.is_file() and p.match('*.py'):
        file_list.append(str(p))

    yield from file_list

# --------------------------测试----------------------
a = file_catch('F:\python-14\zhangjingwen')
for x in a:
    print(x)

# F:\python-14\zhangjingwen\week1\test.py
# F:\python-14\zhangjingwen\week10\send email.py
# F:\python-14\zhangjingwen\week2\Fibonacci.py
# F:\python-14\zhangjingwen\week2\keys generator.py
# F:\python-14\zhangjingwen\week3\Element judgement.py
# F:\python-14\zhangjingwen\week3\words counting.py
# F:\python-14\zhangjingwen\week4\Palindrome Number.py
# F:\python-14\zhangjingwen\week4\random number.py
# F:\python-14\zhangjingwen\week5\commodity choose.py
# F:\python-14\zhangjingwen\week6\job of week6.py
# F:\python-14\zhangjingwen\week7\job of week7.py
# F:\python-14\zhangjingwen\week8\list_element_find.py
# F:\python-14\zhangjingwen\week8\string match.py
# F:\python-14\zhangjingwen\week9\job of week9.py


