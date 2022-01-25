# 카드를 합친 후 더한 값을 공유하니까
# 그리디 쌉가능
# 더한 값을 다시 넣을 때는 힙큐 쓰면 좋을듯
import heapq

n, m = map(int,input().split())
nums = list(map(int,input().split()))

nums.sort()

for _ in range(m):
    a, b = heapq.heappop(nums), heapq.heappop(nums)
    heapq.heappush(nums, a+b)
    heapq.heappush(nums, a+b)
print(sum(nums))