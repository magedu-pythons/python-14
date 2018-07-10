from itertools import takewhile, islice

# The first method to print fabonacci sequence.
first, second = 0, 1
print(first, second, end=' ')

while 1:
    result = first + second
    first, second = second, result

    if result > 100:
        print()
        break
    else:
        print(result, end=' ')

# The second method to print fabonacci sequence.
fib_list = [0, 1]
index = 0
while True:
    new_number = fib_list[index] + fib_list[index + 1]
    index += 1
    if new_number > 100:
        break
    else:
        fib_list.append(new_number)

print(str(fib_list))


# fabonacci sequence with generator.
def fabonacci():
    x, y = 0, 1
    while True:
        yield x
        x, y = y, x + y


num = 100
print(list(takewhile(lambda x: x < num, fabonacci())))
print(next(filter(lambda x: x > num, fabonacci())))
print(next(islice(fabonacci(), num, None)))
