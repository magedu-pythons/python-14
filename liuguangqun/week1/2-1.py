a = 1
b = 1
c = 0
while True:
    print(a)
    c = a + b
    a = b
    b = c
    if a >= 100:
        break
