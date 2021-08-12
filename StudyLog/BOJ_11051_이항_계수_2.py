n,k = map(int,input().split())
k = min(k,n-k)
if k==0:
    print(1)
else:
    res = 1
    for i in range(k):
        res = res * (n-i)
    for i in range(2,k+1):
        res = res // i

    print(res % 10007)


# def fact(n):
#     if n<=1:
#         return 1
#     else:
#         return n*fact(n-1)

# print(fact(n)//fact(k)//fact(n-k) % 10007)