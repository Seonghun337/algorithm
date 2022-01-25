def ptrMat(arr):
    for line in arr:
        print(*line)

import sys
from collections import deque
import copy

n,m = map(int,input().split())
mat = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
dxdys = [(1,0),(-1,0),(0,1),(0,-1)]

cnt = 0
n_area = 0
n_cheese = sum([sum(mat[i]) for i in range(n)])


while True:
    backup = copy.deepcopy(mat)

    visited = [[0]*m for _ in range(n)]
    # 0,0은 무조건 비어있음
    queue = deque([(0,0)])
    visited[0][0] = 1

    while queue:
        y,x = queue.popleft()

        for dxdy in dxdys:
            dx,dy = dxdy
            nx,ny = x+dx, y+dy
            if 0 <= nx < m and 0 <= ny < n and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                if mat[ny][nx] == 1:
                    n_cheese -= 1
                    mat[ny][nx] = 0
                elif mat[ny][nx] == 0:
                    queue.append((ny,nx))
    cnt += 1
    if n_cheese == 0:
    
        # backup으로 영역 개수 체크
        visited = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if visited[i][j] == 0 and backup[i][j] == 1:
                    n_area += 1

                    queue = deque([(i,j)])
                    visited[i][j] = 1
                    while queue:
                        y,x = queue.popleft()
                        for dxdy in dxdys:
                            dx,dy = dxdy
                            nx,ny = x + dx, y + dy
                            if 0 <= nx < m and 0 <= ny < n and visited[i][j] == 0 and backup[i][j] == 1:
                                visited[i][j] = 1
                                queue.append((i,j))

        break


print(cnt)
print(n_area)