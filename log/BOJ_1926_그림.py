from collections import deque

n,m = map(int,input().split())
mat = [list(map(int,input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

dxdys = [(1,0),(-1,0),(0,1),(0,-1)]

cnt = 0
answer = 0

for i in range(n):
    for j in range(m):
        if mat[i][j] == 1 and visited[i][j] == 0:
            cnt += 1
            queue = deque()
            queue.append((i,j))
            visited[i][j] = 1
            S = 1
            while queue:
                y,x = queue.popleft()
                for dxdy in dxdys:
                    dx,dy = dxdy
                    ny,nx = y+dy, x+dx
                    if 0 <= ny < n and 0 <= nx < m and mat[ny][nx] == 1 and visited[ny][nx] == 0:
                        S += 1
                        visited[ny][nx] = 1
                        queue.append((ny,nx))
            answer = max(answer, S)

print(cnt)
print(answer)