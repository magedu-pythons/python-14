import random
str_set = []
for i in range(65,91):
    str_set.append(chr(i))
for _ in range(48,58):
    str_set.append(chr(_))
for _ in range(97,123):
    str_set.append(chr(_))


codelist = []
while True:
    random.shuffle(str_set)

    str = ''
    for _ in range(len(str_set)):
        str += "".join(str_set[_])

    code = ''
    count = 0
    for _ in str:
        count += 1
        if count <= 5:
            code += _
    if code not in codelist:
        codelist.append(code)
    if len(codelist) == 200:
        break
print(codelist)