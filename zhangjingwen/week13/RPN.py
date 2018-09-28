# 3、 将逆转波兰式转化为中序表达式（自行查询逆波兰式、中序表达式相关资料）
# 举例: 输入 {"5", "8", "4", "/", "+"}，输出 "(5+(8/4))"


def trans(src: str):
    src_stack = []

    for x in src:
        if x not in ['+', '-', '*', '/']:
            src_stack.append(x)
        else:
            num1 = src_stack.pop()
            num2 = src_stack.pop()
            result = '(' + num2 + x + num1 + ')' if x != src[-1] else num2 + x + num1
            src_stack.append(result)
    res = ''.join(src_stack)
    return res


# test
print(trans('584/+'))       # 5+(8/4)
print(trans('ab+c*'))       # (a+b)*c
print(trans('45*89*+5/'))   # ((4*5)+(8*9))/5
print(trans('54+1*'))         # (5+4)*1

# 中序表达式转换为逆波兰表达式


def polish(src: str):
    op_stack = ['#']
    result = []
    op_range = {'+': 1, '-': 1, '*': 2, '/': 2, '#': 0}

    for x in src:
        if x not in op_range:
            if x == '(':
                op_stack.append(x)
            elif x == ')':
                for y in op_stack[::-1]:
                    if y != '(':
                        result.append(op_stack.pop())
                    else:
                        break
                op_stack.pop()
            else:
                result.append(x)
        else:
            while True:
                for i in op_stack[::-1]:
                    if i != '(':
                        tmp = i
                        break
                if op_range[x] > op_range[tmp]:
                    op_stack.append(x)
                    break
                else:
                    result.append(op_stack.pop())

    for x in op_stack[::-1]:
        if x != '#':
            result.append(op_stack.pop())

    res = ''.join(result)
    return res


# test
print(polish('5+(8/4)'))            # 584/+
print(polish('(a+b)*c'))            # ab+c*
print(polish('((4*5)+(8*9))/5'))    # 45*89*+5/
print(polish('(5+4)*1'))            # 54+1*




