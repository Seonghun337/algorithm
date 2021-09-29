n = int(input())
nums = list(map(int,input().split()))

dp = [[0]*21 for _ in range(n-1)]

for i in range(n-1):
    if i == 0:
        dp[i][nums[0]] = 1
        continue

    for j in range(21):
        if dp[i-1][j] > 0:
            if j + nums[i] <= 20:
                dp[i][j + nums[i]] += dp[i-1][j]
            
            if j - nums[i] >= 0:
                dp[i][j - nums[i]] += dp[i-1][j]


# print(dp)
# print(sum(dp[-1]))

print(dp[-1][nums[-1]])


# for line in dp:
#     print(*line)