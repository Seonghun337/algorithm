T = int(input())

for _ in range(T):
    n = int(input())

    nums = list(map(int,input().split()))
    now = [x for x in range(1,n+1)]

    cnt = 0

    for i in range(n):
        if now[i] != nums[i]:
            k = now.index(nums[i])
            while now[i] != nums[i]:
                tmp = now[k]
                now[k] = now[k-1]
                now[k-1] = now[tmp]
                cnt += 1
    
    print(cnt)
