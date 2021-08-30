# 왼쪽 인덱스순서대로 오른쪽 원소를 나열했을 때,
# 원소를 몇 개 빼서 단조 증가하도록 만들어야 함.

# 예제 입력
# 8 2 9 1 4 6 7 10
# 예제 답
# 2 4 6 7 10
# 예시 말고 8 9 10 1 11 12 인 경우도 있음


# dp[j] = j개 증가하는 부분수열을 만드는 경우의 수 중 가장 작은 마지막 원소
# 앞에서부터 확인하면서
# dp[k] 보다 nums[i] 값이 크면 (뒤에 놓을 수 있으면) 검사

import sys
import heapq
n = int(input())

tups = []

for _ in range(n):
    heapq.heappush(tups,tuple(map(int,input().split())))

nums = []
for _ in range(n):
    nums.append(heapq.heappop(tups)[1])

max_len = 1

INF = int(1e9)
dp = [INF for _ in range(101)]
dp[0] = 0

for num in nums:
    for i in range(max_len+1):
        if num > dp[i]:
            dp[i+1] = min(dp[i+1], num)
            max_len = max(max_len, i+1)
print(n-max_len)

# print(dp)
# print(max_len)
