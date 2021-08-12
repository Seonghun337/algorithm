import heapq, sys
# 그냥 input은 안되고 sys.stdin.readline 쓰니까 통과
# input이 10000개 넘으면 그냥 readline 쓰자
n = int(sys.stdin.readline().rstrip())
inputs = []
for _ in range(n):
    inputs.append(int(sys.stdin.readline().rstrip()))

queue = []

for i in inputs:
    if i == 0:
        if len(queue) > 0:
            print(heapq.heappop(queue))
        else:
            print(0)
    else:
        heapq.heappush(queue, i)