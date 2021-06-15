import sys

n = int(input())
nums = list(map(int,sys.stdin.readline().rstrip().split()))

# head,tail = 0
# sum = nums[0]
dp = [-1 for _ in range(n)]
dp[0] = nums[0]
for i in range(1,n):
    dp[i] = max(dp[i-1]+nums[i],nums[i])

print(max(dp))
#dp(k) = k번째에서 끝나는 연속 수열 중 합 최대인 수열
#dp(k+1) = dp(k)+a[k+1] or a[k+1]