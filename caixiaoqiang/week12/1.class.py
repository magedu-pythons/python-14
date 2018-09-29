# 实现一个可迭代的类
class Prime:
    def __init__(self):
        self.items = []

    def __call__(self, index):
        return self[index]

    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, index):
        self.items = []
        if index <= 0:
            return 'No value !'
        log = 0
        while True:
            if not self.items:
                self.items.append(1)
                log += 1
                continue
            if self.items[log-1] + 2 > index:
                break
            self.items.append(self.items[log - 1] + 2)
            log += 1
        return self.items


p = Prime()
while True:
    try:
        val = int(input("打印一定范围内的奇数：1—"))
        break
    except:
        print("输入有误，请重新输入！")
p(val)
for v in p:
    print(v, end=" ")
print()







