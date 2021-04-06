from collections import deque

dxdys = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]

def solution(i,x1,y1,x2,y2):
    queue = deque()
    queue.append((x1,y1,0)) # x,y,count

    visited = [[0 for _ in range(i)] for __ in range(i)]
    result = -1

    while 1:
        x,y,cnt = queue.popleft()
        visited[y][x] = 1
        if x==x2 and y==y2:
            result = cnt
            break
        else:
            for dxdy in dxdys:
                dx,dy = dxdy
                nx,ny = x+dx,y+dy
                if nx >= 0 and nx < i and ny >= 0 and ny < i:
                    if visited[ny][nx] == 0:
                        queue.append((nx,ny,cnt+1))

        

    return result

def main():
    T = int(input())
    inputs = []
    for _ in range(T):
        i = int(input())
        x1,y1 = map(int,input().split())
        x2,y2 = map(int,input().split())
        inputs.append((i,x1,y1,x2,y2))

    for case in inputs:
        i,x1,y1,x2,y2 = case
        print(solution(i,x1,y1,x2,y2))

main()