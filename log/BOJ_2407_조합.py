n,m = map(int,input().split())

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)

if m == 0 or n == m:
    print(1)
else:
    print(fact(n)//fact(n-m)//fact(m))