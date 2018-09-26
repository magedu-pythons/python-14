#实现一个可迭代的类

class Iter:
    def __init__(self):
        self.item=[1,2]

    def __iter__(self):
        return iter(self.item)


for i in Iter():
    print(i)