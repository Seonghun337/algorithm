#21.02.04

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

#n : 노드의 개수, m : 간선의 개수
n,m = map(int,input().split())
startNode = int(input())
edges = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, w = map(int,input().split())
    edges[a].append((b,w))


queue = []
mindst = [INF for _ in range(n+1)]
visited = []

heapq.heappush(queue,(0,startNode))
mindst[startNode] = 0

while len(queue) > 0:
    aw, a = heapq.heappop(queue)
    if mindst[a] < aw:
        continue

    for adjEdge in edges[a]:
        b, bw = adjEdge
        if aw+bw < mindst[b]:
            mindst[b] = aw+bw
            heapq.heappush(queue,(mindst[b],b))

    # visited.append(a)

for answer in mindst[1:]:
    if answer==INF:
        print('INF')
    else:
        print(answer)