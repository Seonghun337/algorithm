n = int(input())
wines = [int(input()) for _ in range(n)]

if n==1:
    print(wines[0])
    exit(0)
if n==2:
    print(wines[0] + wines[1])
    exit(0)
    
dp = [-1 for _ in range(n)]
dp[0] = wines[0]
dp[1] = wines[0] + wines[1]
dp[2] = max(wines[0]+wines[2],wines[1]+wines[2],dp[1])

for i in range(3,n):
    dp[i] = max(dp[i-3]+wines[i-1]+wines[i],dp[i-2]+wines[i],dp[i-1])

print(dp[n-1])