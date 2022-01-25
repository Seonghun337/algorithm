T = int(input())

inputs = []
for _ in range(T):
    inputs.append(int(input()))

dp = [0 for _ in range(1000001)]
dp[1] = 1
dp[2] = 2
dp[3] = 4
for x in range(4,1000001):
    dp[x] = (dp[x-1] + dp[x-2] + dp[x-3]) % 1000000009


for i in inputs:
    print(dp[i])