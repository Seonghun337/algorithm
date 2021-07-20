def gcd(m,n):
    a = max(m,n)
    b = min(m,n)

    if a % b == 0:
        return b
    else:
        return gcd(b,a%b)
    

a,b = map(int,input().split())

r = gcd(a,b)
print('1'*r)