

L = [1,1]
x = 2
while x < 100:
    y = L[x-1] + L[x-2]
    if y >= 100:
        break
    x = x + 1
    L.append(y)
print(L)

