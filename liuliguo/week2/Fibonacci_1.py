a = 1
b = 1
print(a)
print(b)
while True:
    c = a + b
    a = b
    b = c
    if c >= 100:#设置最大数
        break
    print(c)