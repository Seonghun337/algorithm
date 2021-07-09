n = int(input())

import sys
nums = list(map(int,sys.stdin.readline().rstrip().split()))

dp = [1 for _ in range(n)]

for i in range(len(nums)):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(dp)
print(max(dp))