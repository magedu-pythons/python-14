def fibonacci_1(n):
    if n == 1 or n == 2:
        return 1
    else:
        result = fibonacci_1(n-1) + fibonacci_1(n-2)
        return result


def print1():
    i = 1
    while True:
        fibonacci = fibonacci_1(i)
        if fibonacci > 100:
            break
        print(fibonacci)
        i += 1


def fibonacci_2(n):
    result = 1
    f1 = 1
    f2 = 1
    if n == 1 or n == 2:
        return result
    else:
        for i in range(1, n-1):
            result = f1 + f2
            f1 = f2
            f2 = result
        return result


def print2():
    i = 1
    while True:
        fibonacci = fibonacci_2(i)
        if fibonacci > 100:
            break
        print(fibonacci)
        i += 1


if __name__ == '__main__':
    print1()
    print2()
