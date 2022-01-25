import sys
import heapq
n = int(input())

inputs = []

for _ in range(n):
    inputs.append(int(sys.stdin.readline().rstrip()))

queue = []

for i in inputs:
    if i == 0:
        if len(queue) > 0:
            a = heapq.heappop(queue)
            print(a[0]*a[1])
        else:
            print(0)
    elif i < 0:
        heapq.heappush(queue, (-i,-1))
    else:
        heapq.heappush(queue, (i, 1))