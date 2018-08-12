import random

list = [1,2,3,4,5]
def random_list(src):
    src1 = src
    random.shuffle(src1)
    return src1

new_list = random_list(list)
print(new_list)