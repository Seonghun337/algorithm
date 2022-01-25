# N <= 200
# 가장 긴 증가하는 부분 수열
import sys
import bisect

n = int(input())
nums = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

dp = [] # 길이 i의 부분 수열의 마지막 값 dp[i]

for num in nums:
    i = bisect.bisect_right(dp, num)
    if i == len(dp):
        dp.append(num)
    else:
        dp[i] = num

print(n-len(dp))


# 3 7 5 2 6 1 4
# 3 7 