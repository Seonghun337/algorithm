import sys
n = int(input())

heights = set([0])#[0] 넣어줘야 될 수도
mat = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

# extract unique domain
for line in mat:
    for cell in line:
        heights.add(cell)

cnt_max = -1

dxdys = [(1,0),(-1,0),(0,1),(0,-1)]

#포함해서 잠기는 걸로
for height in heights:
    cnt = 0
    visited = [[-1 for _ in range(n)] for __ in range(n)]

    for i in range(n):
        for j in range(n):
            if mat[i][j] > height and visited[i][j] == -1:
                cnt = cnt + 1
                stack = [(i,j)]
                visited[i][j] = 1
                while stack:
                    y,x = stack.pop()
                    for dxdy in dxdys:
                        dx,dy = dxdy
                        ny,nx = y+dy, x+dx
                        if 0 <= ny < n and 0 <= nx < n and visited[ny][nx] == -1 and mat[ny][nx] > height:
                            visited[ny][nx] = 1
                            stack.append((ny,nx))

    if cnt_max < cnt:
        cnt_max = cnt


print(cnt_max)