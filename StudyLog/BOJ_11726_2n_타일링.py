def rec(n,dp):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if dp[n] != -1:
        return dp[n]
    else:
        new = rec(n-2,dp) + rec(n-1,dp)
        dp[n] = new
        return new

num = int(input())
dp = [-1 for _ in range(num+1)]

print(rec(num,dp) % 10007)


