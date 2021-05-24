import sys
input = sys.stdin.readline

m,n = map(int,input().rstrip().split())
box = []
for _ in range(n):
    box.append(list(map(int,input().rstrip().split())))

dxdys = [(1,0),(-1,0),(0,1),(0,-1)]

from collections import deque

queue = deque()

visited = [[0 for _ in range(m)] for __ in range(n)]

#search start point
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append((i,j,0))
            visited[i][j] = 1

last_cnt = 0

while len(queue) > 0:
    y,x,d = queue.popleft()
    last_cnt = d
    for dxdy in dxdys:
        dy,dx = dxdy
        ny,nx = y+dy,x+dx
        if 0 <= ny < n and 0 <= nx < m:
            if visited[ny][nx] == 0 and box[ny][nx] == 0:
                queue.append((ny,nx,d+1))
                visited[ny][nx] = 1
                box[ny][nx] = 1

    # print(box)

#check
isOk = 1
for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            isOk = 0

if isOk:
    print(last_cnt)
else:
    print(-1)