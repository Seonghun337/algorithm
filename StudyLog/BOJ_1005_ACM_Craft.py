import sys
from collections import defaultdict, deque
import copy

def solution(n,m,nodes,edges,indegree,w):
    # 위상 정렬

    times = copy.deepcopy(nodes) # 누적 시간
    
    queue = deque()
    
    # 진입차수가 0인 것들 큐에 넣기
    for x in range(1,n+1):
        if indegree[x] == 0:
            queue.append(x)

    while queue:
        x = queue.popleft()

        for b in edges[x]:

            indegree[b] = indegree[b] - 1
            times[b] = max(times[b],times[x]+nodes[b])
            if indegree[b] == 0:
                queue.append(b)

    return times[w]





ans = []

#input
T = int(input())
for _ in range(T):
    n,m = map(int,sys.stdin.readline().rstrip().split())
    nodes = [0] + list(map(int,sys.stdin.readline().rstrip().split()))
    
    # print(nodes)
    edges = defaultdict(list)
    indegree = [0 for _ in range(n+1)]

    for _ in range(m):
        a,b = map(int,sys.stdin.readline().rstrip().split())
        edges[a].append(b)
        indegree[b] = indegree[b] + 1

    w = int(input())


    ans.append(solution(n,m,nodes,edges,indegree,w))

    

for an in ans:
    print(an)