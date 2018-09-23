'''1、实现一个可迭代的类'''
class List:
    def __init__(self):
        self.value = []
        self.i = -1

    def append(self,num):
        self.value.append(num)

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.i >= len(self.value) :
            raise StopIteration
        return self.value[self.i]

l = List()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
for x in l.__iter__():
    print(x)
