n,m = map(int,input().split())
from collections import defaultdict, deque
edges = defaultdict(list)

for _ in range(m):
    a,b = map(int,input().split())
    edges[a].append(b)

dp = [0 for _ in range(n+1)]

for startNode in range(1,n+1):
    visited = [0 for _ in range(n+1)]
    queue = deque([startNode])
    visited[startNode] = 1

    while queue:
        a = queue.popleft()
        for b in edges[a]:
            if visited[b]==0:
                dp[b] = dp[b] + 1
                visited[b] = 1
                queue.append(b)

# print(dp)

M = max(dp)
answer = []
for i in range(1,n+1):
    if dp[i]==M:
        answer.append(i)

print(*answer)

            

