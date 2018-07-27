import random
lst = [random.randint(1, 100) for i in range(20)]
print(lst)
lst.sort()
print(lst[-1], lst[-2], lst[-3])
