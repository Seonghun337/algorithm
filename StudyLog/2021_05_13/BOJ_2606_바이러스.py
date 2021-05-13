from collections import deque

n = int(input())
m = int(input())
adj = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)

queue = deque()
queue.append(1)
visited[1] = 1
cnt = 0

while len(queue) > 0:
    src = queue.popleft()

    for dst in adj[src]:
        if visited[dst] == 0:
            visited[dst] = 1
            queue.append(dst)
            cnt = cnt + 1
        else:
            continue

print(cnt)