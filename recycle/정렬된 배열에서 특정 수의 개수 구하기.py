n,m = map(int,input().split())

nums = list(map(int,input().split()))

def upper(a=0,b=n):
    
    while a < b:
        mid = (a+b) // 2

        if nums[mid] > m:
            b = mid
        else:
            a = mid+1


    return b

def lower(a=0,b=n):

    while a < b:
        mid = (a+b) // 2

        if nums[mid] >= m:
            b = mid
        else:
            a = mid+1

    return b

up = upper()
lo = lower()

if up > lo:
    print(up-lo)
else:
    print(-1)