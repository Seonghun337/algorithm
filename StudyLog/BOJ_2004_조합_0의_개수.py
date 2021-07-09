n,m = map(int,input().split())

def getV(n,k):
    N = 0
    p = 1
    while 1:
        v = n//(k**p)
        if v == 0:
            break
        else:
            N = N + v
            p = p + 1
    return N

# m = min(m,n-m)
v5 = getV(n,5) - getV(n-m,5) - getV(m,5)
v2 = getV(n,2) - getV(n-m,2) - getV(m,2)
print(min(v5,v2))



