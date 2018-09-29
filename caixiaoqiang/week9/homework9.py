# 1.请实现函数new_counter，使得调用结果如下：
# c1 = new_counter(10)
# c2 = new_counter(20)
# print(c1(), c2(), c1(), c2())
# outputs:
# 11 21 12 22


def new_counter(num):
    def adorn():
        nonlocal num
        num += 1
        return num
    return adorn


c1 = new_counter(10)
c2 = new_counter(20)
print(c1(), c2(), c1(), c2())


# 2.实现一个函数，输入字符串，判断字符串，判断该字符串是否含有重复字符

def judge_str(fn):
    for i in range(len(fn)):
        if fn.count(fn[i]) > 1:
            print("Duplicate Characters!")
            break
    else:
        print("No Duplicate Characters!")


while True:
    string = input("Please enter a string:")
    if string == 'end':
        break
    judge_str(string)
