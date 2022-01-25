from collections import defaultdict,deque

n = int(input())
m = int(input())

edges = defaultdict(list)

for _ in range(m):
    a,b = map(int,input().split())
    edges[a].append(b)
    edges[b].append(a)


queue = deque([(0,1)]) # w, node
friends = set()

while queue:
    w,a = queue.popleft()
    friends.add(a)

    if w < 2:
        for b in edges[a]:
            queue.append((w+1,b))

friends.remove(1)
# print(friends)
print(len(friends))