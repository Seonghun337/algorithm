n = int(input())

from collections import defaultdict,deque

edges = defaultdict(list)

for _ in range(n-1):
    a,b = map(int,input().split())
    edges[a].append(b)
    edges[b].append(a)

nodes = [-1 for _ in range(n+1)] #index : 노드번호,  value : 부모

queue = deque()
queue.append(1)

while queue:
    a = queue.pop()
    
    for b in edges[a]:
        if nodes[b] == -1: #아직 부모 못찾았으면
            nodes[b] = a
            queue.append(b)


for a in nodes[2:]:
    print(a)