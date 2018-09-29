'''
3.将逆转波兰式转化为中序表达式（自行查询逆波兰式、中序表达式相关资料）
举例：输入{"5","8","4","/","+"}, 输出"(5+(8/4))"
'''

def Func(rpn):
    val_rpn = []
    str_rpn = ''
    oper = ['+', '-', '*', '/']
    for item in rpn:
        if item in oper:
            right = val_rpn.pop()
            left = val_rpn.pop()
            str_rpn = '('+ left + item + right + ')'
            val_rpn.append(str_rpn)
        else:
            val_rpn.append(item)
    print("逆波兰式：{}".format(rpn))
    print("中序表达式：{}".format(str_rpn))
rpn1 = ["1", "2", "3", "4", "-", "*", "+", "5", "6", "/", "-"] # ((1+(2*(3-4)))-(5/6))
rpn2 = ["5","8","4","/","+"]
Func(rpn1)
Func(rpn2)