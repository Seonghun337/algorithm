import sys
n = int(input())
map_ = [list(map(int,list(sys.stdin.readline().rstrip()))) for _ in range(n)]

visited = [[0 for _ in range(n)] for __ in range(n)]

dxdys = [(1,0), (-1,0), (0,1), (0,-1)]


def search(i,j):
    cnt = 1
    stack = []
    stack.append((j,i))
    visited[i][j] = 1

    while len(stack) > 0:
        x,y = stack.pop()
        
        for dxdy in dxdys:
            dx,dy = dxdy
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n:
                if map_[ny][nx] == 1 and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    stack.append((nx,ny))
                    cnt = cnt + 1
                    # print(ny,nx)
    
    # print('------------')
    return cnt


cnt = 0
answers = []
for i in range(n):
    for j in range(n):
        if map_[i][j] == 1 and visited[i][j] == 0:
            answers.append(search(i,j))
            cnt = cnt + 1

print(cnt)
answers.sort()
for answer in answers:
    print(answer)

# print(search(0,1),map_,visited)