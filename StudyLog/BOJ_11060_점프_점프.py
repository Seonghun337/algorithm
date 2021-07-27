n = int(input())

import sys
nums = list(map(int,sys.stdin.readline().rstrip().split()))

INF = int(1e9)

res = [INF for _ in range(n)]
res[0] = 0

for i in range(n):
    for j in range(1,nums[i]+1):
        if i+j < n:
            res[i+j] = min(res[i+j],res[i]+1)
        else:
            break

print(res)

if res[-1] == INF:
    print(-1)
else:
    print(res[-1])
