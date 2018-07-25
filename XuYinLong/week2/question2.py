#1th solution
a=0
b=1
print(0)
print(1)
while True:
    c=a+b
    if c>100:
        break
    a=b
    b=c
    print(c)

# 2th soulution
a = [1, 1]
for i in range(2, n):
    a.append(a[i - 2] + a[i - 1])
    if a[i] > 100:
        a.pop(i)
        print(a)
        break
