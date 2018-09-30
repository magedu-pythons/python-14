# 将中序转换成逆波兰序  he  计算逆波兰序的结果
class Stuck:                                #创造一个栈
    def __init__(self):
        self.stuck = []
    def is_empty(self):
        return self.stuck == []
    def push(self,str):                     #压栈
        self.stuck.append(str)
    def pull(self):                         #出栈
        return self.stuck.pop()

# 将中序转换成逆波兰序
formula = "1+((2+3^2)*4)-5"
def nibolan(formula):
    s2 = Stuck()
    s1 = Stuck()
    t1 = ["^"]
    t2 = ['*','/']
    t3 = ['+','-']
    for i in formula:
        if i.isdigit():
            s2.push(i)
        else:
            if i == "(" or s1.is_empty():
                s1.push(i)
            elif i in t1:
                while s1.stuck[-1] in t1:
                    s2.push(s1.pull())
                    if s1.is_empty():
                        break
                s1.push(i)
            elif i in t2:
                if s1.stuck[-1] in t2+t3:
                    s2.push(s1.pull())
                s1.push(i)
            elif i in t3:
                while s1.stuck[-1] in t3+t2+t1:
                    s2.push(s1.pull())
                    if s1.is_empty():
                        break
                s1.push(i)
            elif i == ")":
                while s1.stuck[-1] != "(":
                    s2.push(s1.pull())
                s1.pull()
    while not s1.is_empty():
        x = s1.pull()
        if x != '(':
            s2.push(x)
    return s2.stuck
x = nibolan(formula)
print(x)

def count_nibolan(formula):
    s2 = Stuck()
    for i in formula:
        if i.isdigit():
            s2.push(int(i))
        else:
            x = s2.pull()
            y = s2.pull()
            if i == '*':
                result = x*y
            elif i == '/':
                result = x/y
            elif i == '+':
                result = x+y
            elif i == '-':
                result = y-x
            elif i == '^':
                result = y**x
            s2.push(result)
    return s2.pull()
print(count_nibolan(x))