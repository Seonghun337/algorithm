n = int(input())
ta,tb = map(int,input().split())

m = int(input())

from collections import defaultdict
edges = defaultdict(list)

for _ in range(m):
    a,b = map(int,input().split())
    edges[a].append(b)
    edges[b].append(a)

from collections import deque
queue = deque()
queue.append((ta,0))

visited = [-1 for _ in range(n+1)]
visited[ta] = 1


answer = -1
while queue:
    a, d = queue.popleft()
    if a == tb:
        answer = d
        break

    for b in edges[a]:
        if visited[b] == -1:
            queue.append((b,d+1))
            visited[b] = 1


print(answer)
