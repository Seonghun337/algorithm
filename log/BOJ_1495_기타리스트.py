from collections import deque


n,s,m = map(int,input().split())
v_list = list(map(int,input().split()))

dp = [[0] * (m+1) for _ in range(n+1)]

dp[0][s] = 1

for i in range(1,n+1):
    for j in range(m+1):
        # print(dp[i])
        if j-v_list[i-1] >= 0 and dp[i-1][j-v_list[i-1]] == 1:
            dp[i][j] = 1

        if j+v_list[i-1] <= m and dp[i-1][j+v_list[i-1]] == 1:
            dp[i][j] = 1

# print(dp)

for i in range(m,-1,-1):
    if dp[-1][i] == 1:
        print(i)
        break
else:
    print(-1)