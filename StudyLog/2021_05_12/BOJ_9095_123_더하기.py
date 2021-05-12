n = int(input())
inputs = [int(input()) for _ in range(n)]

dp = [-1 for _ in range(11)]

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4,len(dp)):
    new = 0
    if i-1 > 0:
        new = dp[i-1]
    if i-2 > 0:
        new = new + dp[i-2]
    if i-3 > 0:
        new = new + dp[i-3]

    dp[i] = new


for i in inputs:
    print(dp[i])