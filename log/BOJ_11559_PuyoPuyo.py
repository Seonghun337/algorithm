from collections import deque

n = 12
m = 6

mat = [list(input()) for _ in range(n)]

dxdys = [(1,0),(-1,0),(0,1),(0,-1)]
def search():
    visited = [[0]*m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if mat[i][j] != '.' and visited[i][j] == 0:
                group = [(i,j)]
                group_cnt = 1
                color = mat[i][j]
                queue = deque([(i,j)])
                visited[i][j] = 1
                while queue:
                    y,x = queue.popleft()
                    visited[y][x] = 1

                    for dxdy in dxdys:
                        dx,dy = dxdy
                        nx,ny = x + dx, y + dy
                        if 0<=nx<m and 0<=ny<n and visited[ny][nx] == 0 and mat[ny][nx] == color:
                            queue.append((ny,nx))
                            group.append((ny,nx))
                            group_cnt += 1
                if group_cnt >= 4:
                    for yx in group:
                        y,x = yx
                        mat[y][x] = '.'
                    cnt += 1
    return cnt

def fall():
    for j in range(m):
        for i in range(n-1,-1,-1):
            if mat[i][j] == '.':
                for k in range(i-1,-1,-1):
                    if mat[k][j] != '.':
                        # swap mat[i][j], mat[k][j]
                        tmp = mat[i][j]
                        mat[i][j] = mat[k][j]
                        mat[k][j] = tmp
                        break
                else:
                    break

def prt():
    for line in mat:
        print(*line)


cnt = 0
while True:
    # prt()
    if search() == 0:
        break
    else:
        # prt()
        cnt += 1
        fall()
        # prt()
    
    

print(cnt)

