#打印九九乘法表

for row in range(1,10):
    for col in range(1,row+1):
        print(str(col) + '*' + str(row) + '=' + str(row*col),end='\t')
    print('\n')

