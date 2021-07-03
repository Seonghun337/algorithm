n,m = map(int,input().split())
nums = list(map(int,input().split()))

a = 0
b = 0

cnt = 0

while a <= b < n:
    if a == b:
        if a == m:
            cnt = cnt + 1
        b = b + 1
        continue
    
    s = sum(nums[a:b+1])
    if s == m:
        cnt = cnt + 1
        b = b + 1
    elif s < m:
        b = b + 1
    else:
        a = a + 1

print(cnt)