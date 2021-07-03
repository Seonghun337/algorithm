import sys

n = int(input())
nums = list(map(int,sys.stdin.readline().rstrip().split()))

dp = [1 for _ in range(n)]


for i in range(n):
    for j in range(i+1):
        if nums[i] < nums[j]:
            dp[i] = max(dp[i],dp[j]+1)

# print(dp)
print(max(dp))