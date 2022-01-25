# from collections import deque

# n,m = map(int,input().split())

# dsts = [[] for _ in range(n+1)]

# for _ in range(m):
#     a,b = map(int,input().split())
#     dsts[a].append(b)
#     dsts[b].append(a)

# visited = [0 for _ in range(n+1)]

# cnt = 0

# for x in range(1,n+1):
#     if visited[x] == 0:
#         queue = deque()
#         queue.append(x)
#         while len(queue) > 0:
#             a = queue.pop()
#             for b in dsts[a]:
#                 if visited[b] == 0:
#                     queue.append(b)
#                     visited[b] = 1
#         cnt = cnt + 1

# print(cnt)



from collections import deque
from collections import defaultdict

n,m = map(int,input().split())

# dsts = [[] for _ in range(n+1)]
dsts = defaultdict(list)


for _ in range(m):
    a,b = map(int,input().split())
    dsts[a].append(b)
    dsts[b].append(a)

visited = [0 for _ in range(n+1)]

cnt = 0

for x in range(1,n+1):
    if visited[x] == 0:
        queue = deque()
        queue.append(x)
        while len(queue) > 0:
            a = queue.pop()
            for b in dsts[a]:
                if visited[b] == 0:
                    queue.append(b)
                    visited[b] = 1
        cnt = cnt + 1

print(cnt)
