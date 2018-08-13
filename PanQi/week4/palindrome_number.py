var = int(input('>>>'))

if var >= 10000 and var <= 99999:
    print ('OK,这是个五位数')
else:
    print ('请重新输入一个五位数！')

lisa = list(str(var))  
lisa.reverse()
rav = int("".join(lisa))

if var == rav:
    print ('这是一个回文数。')
else:
    print ('这不是一个回文数。')
