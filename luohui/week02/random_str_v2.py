import string
from time import time

str_set = string.digits + string.ascii_letters


def generate_str(str_len):
    while True:
        res = ''
        for _ in range(str_len):
            index = int(str(time()).split('.')[1]) % len(str_set)
            res += str_set[index]
        yield res


num = 200
result = set()
for x in generate_str(5):
    result.add(x)
    if len(result) >= num:
        break

print(result)
