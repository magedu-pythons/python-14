from time import time

digits = [chr(x) for x in range(48, 58)]
ascii_lowercase = [chr(y) for y in range(97, 123)]
ascii_uppercase = [chr(z) for z in range(65, 91)]
str_set = digits + ascii_lowercase + ascii_uppercase


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
