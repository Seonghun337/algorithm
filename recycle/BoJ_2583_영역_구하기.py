import sys
from collections import deque

m,n,k = map(int,input().split())

mat = [[0 for _ in range(n)] for _ in range(m)]


for _ in range(k):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().rstrip().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            mat[i][j] = 1

visited = [[-1 for _ in range(n)] for __ in range(m)]

cnt_n_area = 0
s_area = []

dxdys = [(1,0),(-1,0),(0,1),(0,-1)]

for i in range(m):
    for j in range(n):
        if mat[i][j] == 0 and visited[i][j] == -1:
            cnt_n_area = cnt_n_area + 1

            cnt_cell = 1
            visited[i][j] = 1
            queue = deque([(i,j)])
            while queue:
                y,x = queue.popleft()
                for dxdy in dxdys:
                    dx,dy = dxdy
                    nx,ny = x + dx, y + dy
                    if 0<=nx<n and 0<=ny<m and visited[ny][nx] == -1 and mat[ny][nx] == 0:
                        cnt_cell = cnt_cell + 1
                        visited[ny][nx] = 1
                        queue.append((ny,nx))

            s_area.append(cnt_cell)

s_area.sort()
print(cnt_n_area)
print(*s_area)