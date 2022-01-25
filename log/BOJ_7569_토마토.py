from collections import deque
import sys

m,n,h = map(int,input().split())

box = [[list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)] for __ in range(h)]

dxdydzs = [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]

visited = [[[-1 for _ in range(m)] for __ in range(n)] for ___ in range(h)]
queue = deque()

n_putTomato=0
for k in range(h):
    for i in range(n):
        for j in range(m):
            if box[k][i][j] == 1:
                queue.append((k,i,j,0))
                visited[k][i][j] = 1
            elif box[k][i][j] == 0:
                n_putTomato = n_putTomato + 1

max_w = -1

n_changedPutTomato = 0
while queue:
    z,y,x,w = queue.popleft()

    if w > max_w:
        max_w = w

    for dxdydz in dxdydzs:
        dx,dy,dz = dxdydz
        nx,ny,nz = x+dx, y+dy, z+dz
        if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h and visited[nz][ny][nx] == -1 and box[nz][ny][nx] == 0 :
            n_changedPutTomato = n_changedPutTomato + 1
            box[nz][ny][nx] = 1
            visited[nz][ny][nx] = 1
            queue.append((nz,ny,nx,w+1))


if n_putTomato != n_changedPutTomato:
    print(-1)
else:
    print(max_w)


