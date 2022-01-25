n = int(input())

dp = [1 for _ in range(10)]

for _ in range(n-1):
    for i in range(10):
        dp[i] = sum(dp[i:10])

print(sum(dp) % 10007)