m = [1,2,1,3,4,5]
n = [2,3,4,1,2]

def x(m,n,k):
    x_count = m+n
    return x_count[k-1]

print(x(m,n,7))
