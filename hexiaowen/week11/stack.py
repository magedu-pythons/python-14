class Stack:
    def __init__(self):
        self.list = []

    def append(self,num):
        self.list.append(num)

    def pop(self):
        self.list.pop()

    def show(self):
        return self.list



s = Stack()
s.append(1)
s.append(2)
print(s.show())