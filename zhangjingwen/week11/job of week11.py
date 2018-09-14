#
# # 1、实现数据结构stack(栈)，并实现它的append，pop方法【动手查询相关资料理解stack特点以及与queue区别】
class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

    def __repr__(self):
        return str(self.val)

    __str__ = __repr__

class Stack:
    def __init__(self):
        self.top = None
        self.item = 0

    def __len__(self):
        return self.item

    def __str__(self):
        dest = ''
        for x in self.iter():
            try:
                dest += (str(x.val) + ' ')
            except:
                dest += ('unknown' + ' ')
        return dest

    def iter(self):
        cur = self.top
        while cur:
            yield cur
            cur = cur.next

    def peek(self):           # 返回栈顶元素的值
        try:
            dest = self.top.val
        except:
            dest = None
        return dest

    def push(self, value):    # 入栈
        node = Node(value)
        node.next = self.top
        self.top = node
        self.item += 1

    def pop(self):             # 出栈
        cur = self.top
        if cur is not None:
            self.top = cur.next
            self.item -= 1
            return cur.val


# test

a = Stack()
a.push('abc')
a.push(lambda x: 1)
a.push(4)
a.push(None)

print(a)            # None 4 <function <lambda> at 0x0147F7C8> abc
print(len(a))       # 4
print(a.peek())     # None
print(a.pop())      # None
print(a.pop())      # 4
print(a.pop())      # <function <lambda> at 0x0121F7C8>



# 2、打印出N对合理的括号组合。
# 例如： 当N=3，输出：()()(),()(()),(())(),((()))


def generate(left, right, s, result):
    if left == 0 and right == 0:
        result.append(s)

    if left > 0:
        generate(left-1, right+1, s+'(', result)

    if right > 0:
        generate(left, right-1, s+')', result)

def Parentheses(n):
    result = []
    generate(n, 0, '', result)

    return result

# test
print(Parentheses(3))       # ['((()))', '(()())', '(())()', '()(())', '()()()']
print(Parentheses(2))       # ['(())', '()()']


# 3、根据字典，从一个抹去空格的字符串里面提取出全部单词组合，并且拼接成正常的句子:
# 例如: 输入一个字符串："thisisanexample", 程序输出: "this is an example"
def wordCut(s: str):
    if not s:
        return

    src = {'this': 0, 'is': 0, 'an': 0, 'example': 0}
    cur = ''
    result = []

    for x in s:
        cur += x
        if not cur in src:
            continue
        else:
            result.append(cur)
            cur = ''
    result.append(cur)

    return ' '.join(result)

print(wordCut(''))