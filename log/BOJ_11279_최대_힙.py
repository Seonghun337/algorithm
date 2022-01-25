import heapq
import sys

n = int(sys.stdin.readline())

prtbuf = []
heap = []



for _ in range(n):
    cmd = int(sys.stdin.readline())
    if cmd == 0:
        if len(heap) > 0:
            prtbuf.append(-heapq.heappop(heap))
            # print(-heapq.heappop(heap))
        else:
            prtbuf.append(0)
            # print(0)
    else:
        heapq.heappush(heap,-cmd)
    # print(cmd,heap)

for a in prtbuf:
    print(a)

# print(heap)