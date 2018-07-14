import string
from random import sample


def generate_str(str_len):
    while True:
        yield ''.join(sample(string.digits + string.ascii_letters, str_len))


def generate_passwd(passwd_len):
    return ''.join(sample(string.digits + string.ascii_letters + string.punctuation, passwd_len))


num = 200
result = set()
for x in generate_str(5):
    result.add(x)
    if len(result) >= num:
        break

print(result)
print(generate_passwd(16))
