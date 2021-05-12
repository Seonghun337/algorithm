n = int(input())
steps = [int(input()) for _ in range(n)]

dp = [-1 for _ in range(n+1)]
INF = (1e9)

def rec(n, dp, cnt):
    if n < 0:
        return 0
    if cnt >= 3:
        return -INF
    if dp[n] != -1:
        return dp[n]
    else:
        new = max(rec(n-2,dp,0),rec(n-1,dp,cnt+1)) + steps[n-1]
        dp[n] = new
        return new

print(rec(n,dp,0))
print(dp)