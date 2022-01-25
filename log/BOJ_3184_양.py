r,c = map(int,input().split())
field = [list(input()) for _ in range(r)]

# 바깥 어떻게? 그냥 ㄱ

visited = [[-1 for _ in range(c)] for __ in range(r)]
dxdys = [(-1,0), (1,0), (0,-1), (0,1)]
# def
def search(i,j):
    n_v = 0
    n_o = 0

    stack = []
    stack.append((i,j))
    visited[i][j] = 1
    while stack:
        y,x = stack.pop()
        if field[y][x] == 'v':
            n_v = n_v + 1
        elif field[y][x] == 'o':
            n_o = n_o + 1


        for dxdy in dxdys:
            dx,dy = dxdy
            nx,ny = x+dx, y+dy
            
            try:
                if field[ny][nx] != '#' and visited[ny][nx] == -1:
                    visited[ny][nx] = 1
                    stack.append((ny,nx))
            except IndexError:
                continue

    return n_v, n_o


ans_v = 0
ans_o = 0
for i in range(r):
    for j in range(c):
        if field[i][j] != '#' and visited[i][j] == -1:
            v,o = search(i,j)
            if v >= o:
                ans_v = ans_v + v
            else:
                ans_o = ans_o + o

print(ans_o,ans_v)


