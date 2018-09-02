class New_count:
    '''
    请实现函数 new_counter ，使得调用结果如下：
      c1 = new_counter(10)
      c2 = new_counter(20)
      print（c1(), c2(), c1(), c2()）
      outputs ：
      11 21 12 22
    '''
    def __init__(self,count):
        self.count = count

    def __call__(self):
        self.count += 1
        return self.count

c1 = New_count(10)
c2 = New_count(20)
print(c1(),c2(),c1(),c2())
