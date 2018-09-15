# 打印出N对合理的括号组合。
# 例如： 当N=3，输出：()()(),()(()),(())(),((()))
'''
例：N = 2
                            (  if left
            ((  if left                         ()  if right
                (() if right              ()( if left        ()) if right
                     (()) if right             ()() if right
利用二叉树理解
'''


def bracket(comb, left, right):
    if right == 0:
        print(comb)
    if right > 0 and right > left:
        print("right （剩余:{}, ）剩余:{}, {}".format(left, right, comb))
        bracket(comb + ')', left, right - 1)
    if left > 0:
        print("left （剩余:{}, ）剩余:{}, {}".format(left, right, comb))
        bracket(comb + '(', left - 1, right)


while True:
    try:
        comb = ''
        num = int(input("请输入括号对数："))
        left = right = num
        bracket(comb, left, right)
    except Exception as e:
        print(e)



