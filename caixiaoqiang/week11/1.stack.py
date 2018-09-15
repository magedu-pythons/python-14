#  实现数据结构stack(栈)，并实现它的append，pop方法[手动查询相关资料理解stack特点以及与queue区别]

# 栈（stack）：是限定仅在表尾进行插入或删除操作的线性表。表尾为栈顶，表头为栈底，空表为空栈。
#              是后进先出（last in first out）的线性表（LIFO结构）
# 队列（queue）：是只允许在表头进行删除，表尾进行插入的线性表，表头为队头，表尾为队尾，空表为空队。
#                是先进先出（first in first out）的线性表（FIFO结构）


class Stack:
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            return self.items

    def __repr__(self):
        return repr(self.items)


stack = Stack()
print(stack, type(stack))
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
stack.append(5)
print(stack)


