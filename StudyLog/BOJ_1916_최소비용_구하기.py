#21.02.04

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

edges = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, w = map(int,input().split())
    edges[a].append((b,w))
startNode,endNode = map(int,input().split())

queue = []
mindst = [INF for _ in range(n+1)] # mindst[i] = startNode에서 i번 노드까지의 최소 비용
visited = []

heapq.heappush(queue,(0,startNode))
mindst[startNode] = 0

while len(queue) > 0:
    aw, a = heapq.heappop(queue) # 가장 작은 가중치(비용)을 가진 노드 선택
    if mindst[a] < aw:
        continue

    for adjEdge in edges[a]: # 인접한 모든 노드를 검사하여 더 적은 비용으로 갈 수 있으면 mindst 갱신
        b, bw = adjEdge
        if aw+bw < mindst[b]:
            mindst[b] = aw+bw
            heapq.heappush(queue,(mindst[b],b))

    # visited.append(a)

print(mindst[endNode])
