num1 = 1
num2 = 1
print("first:", end=' ')
print(num1, end=' ')
while num2 < 100:
    print(num2, end=' ')
    p = num2
    num2 = num1 + num2
    num1 = p
print()
print("second:", end=' ')

i = 1
def func(i):
    if i == 1 or i == 2:
        return 1
    else:
        return int(func(i-1) + func(i-2))
while i:
    s = func(i)
    if s < 100:
        print(s, end=' ')
    else:
        break
    i += 1

