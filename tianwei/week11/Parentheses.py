#打印出N对合理的括号组合。
#例如： 当N=3，输出：()()(),()(()),(())(),((()))
#n=4,x=['()()()()','()()(())','(())()()','()(())()','()((()))','((()))()','(())(())','(((())))']

def paren(n:int):
    x = []
    if n==1:
        x=['()']
    if n>1:
        for c in range(1,n):
            tmp='('*c+')'*c
            for i in paren(n-c):
                x.append(i + tmp)
        x.append('('*n+')'*n)
    return x

print(paren(4))

