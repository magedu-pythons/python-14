for i in range(1,10):
    for j in range(1,i+1):
        print('%s x %s = %2s' % (j,i,(i*j)),end='   ')
    print('\n')