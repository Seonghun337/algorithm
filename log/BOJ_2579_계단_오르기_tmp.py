n = int(input())
steps = [int(input()) for _ in range(n)]
dp = {}

def func(n,steps,dp):
    if n in dp.keys():
        return dp[n]

    if n < 0:
        return 0
    if n == 0: 
        dp[0] = steps[0]
        return steps[0]

    new = max(func(n-3,steps,dp)+steps[n-1],func(n-2,steps,dp)) + steps[n]
    dp[n] = new
    return new

print(func(n-1,steps,dp))