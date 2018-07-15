import random
str = [chr(i) for i in range(97,123)] #a-z
STR = [chr(i) for i in range(65,91)] #A-Z
num = [chr(i) for i in range(48,58)] #0-9
for i in range(200):
    s = str + STR + num
    code = ''
    for i in range(5):
        code += random.choice(s)
    print(code)