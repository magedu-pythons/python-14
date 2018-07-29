import random

code_list = [random.randint(1, 100) for _ in range(20)]

def f(fn):
    def wrapper(*code_list):
        a = fn(*code_list)
        return a
    return wrapper
@f # maxnum = f(maxnum)
def maxnum(code_list, max_list=[]):
    if len(max_list) < 3:
        max_num = max(code_list)
        max_list.append(max_num)
        code_list.remove(max_num)
        maxnum(code_list, max_list)
        return max_list
    else:
        return max_list

print(maxnum(code_list))

