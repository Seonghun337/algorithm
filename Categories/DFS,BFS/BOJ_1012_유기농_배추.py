dxdys = [(1,0),(-1,0),(0,1),(0,-1)]

def solution(n,m,positions):
    visited = [[0 for _ in range(m)] for __ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if positions[i][j] == 1 and visited[i][j] == 0:
                cnt = cnt+1
                stack = []
                stack.append((j,i))
                while len(stack) > 0:
                    x,y = stack.pop()
                    visited[y][x] = 1
                    for dxdy in dxdys:
                        dx,dy = dxdy
                        nx,ny = x+dx,y+dy
                        if nx >= 0 and nx < m and ny >= 0 and ny < n:
                            if visited[ny][nx] == 0 and positions[ny][nx] == 1:
                                stack.append((nx,ny))

                # print(visited)
    return cnt

def main():
    T = int(input())
    inputs = []
    for _ in range(T):
        m,n,k = map(int,input().split())
        positions = [[0 for _ in range(m)] for __ in range(n)]
        for __ in range(k):
            x,y = map(int,input().split())
            positions[y][x] = 1

        inputs.append((n,m,positions))

    for c in inputs:
        n,m,positions = c
        print(solution(n,m,positions))
main()