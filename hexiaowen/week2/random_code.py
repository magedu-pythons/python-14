import string
import random
random_code=[]
code=''
i=0
num=string.ascii_letters+string.digits
while i < 200:
    for j in range(5):
        code += random.choice(num)
    if code not in random_code:
        i+=1
        random_code.append(code)
    code=''
for j in range(len(random_code)):
    print(random_code[j])