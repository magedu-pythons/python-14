#将逆波兰序转换成算式
class Stuck:                                #创造一个栈
    def __init__(self):
        self.stuck = []
    def is_empty(self):
        return self.stuck == []
    def push(self,str):                     #压栈
        self.stuck.append(str)
    def pull(self):                         #出栈
        return self.stuck.pop()
x = ["5", "8", "4", "/", "+"]
def count_nibolan(formula):
    s2 = Stuck()
    for i in formula:
        if i.isdigit():
            s2.push(i)
        else:
            x = s2.pull()
            y = s2.pull()
            result = '('+y+i+x+')'
            s2.push(result)
    return s2.pull()
print(count_nibolan(x))