#21.02.03

from collections import deque

def solution(n,m,v,edges):
    adjlst = [[] for _ in range (n+1)]
    for edge in edges:
        adjlst[edge[0]].append(edge[1])
        adjlst[edge[1]].append(edge[0])

    for adjs in adjlst:
        adjs.sort()

    # print(adjlst)
    #DFS
    result_dfs = []
    stack = []


    stack.append(v)
    result_dfs.append(v)

    while True:
        if len(result_dfs) == n or len(stack) == 0:
            break
        
        a = 0

        curNode = stack[-1]
        for nn in adjlst[curNode]:
            if a==1:break
            if nn not in result_dfs:
                result_dfs.append(nn)
                stack.append(nn)
                a = 1
        
        if a == 0:
            stack.pop()
                
    #BFS
    result_bfs = []
    queue = deque()

    queue.append(v)
    result_bfs.append(v)


    while True:
        if len(result_bfs) == n or len(queue) == 0:
            break
        
        curNode = queue.popleft()
        for nn in adjlst[curNode]:
            if nn not in result_bfs:
                result_bfs.append(nn)
                queue.append(nn)

        
    return result_dfs,result_bfs

def main():
    n, m, v = map(int,input().split())
    edges = []
    for i in range(m):
        a,b = map(int,input().split())
        edges.append((a,b))

    r1, r2 = solution(n,m,v,edges)
    print(' '.join(map(str,r1)))
    print(' '.join(map(str,r2)))

main()