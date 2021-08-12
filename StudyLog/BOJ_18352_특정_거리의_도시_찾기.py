# 플로이드 워셜로 풀려고 했으나, O(n^3) 이기 때문에 (n <= 300000)
# 다익스트라로 풀겠습니다.
# 힙큐가 필요하겠네요
# 필요한가요? 가중치가 다 1인데요
# 1차 시도 실패. 지우고 다시


import sys
from collections import defaultdict, deque

n,m,k,x = map(int,sys.stdin.readline().rstrip().split())
edges = defaultdict(list)

for _ in range(m):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    edges[a].append(b)


answer = []


queue = deque()
visited = [-1 for _ in range(n+1)]

queue.append((x,0))
visited[x] = 1

while queue:
    a, w = queue.popleft()
    if w == k:
        answer.append(a)
    elif w > k:
        break

    for b in edges[a]:
        if visited[b] == -1:
            visited[b] = 1
            queue.append((b,w+1))

if answer:
    answer.sort()
    for a in answer:
        print(a)
else:
    print(-1)
            

