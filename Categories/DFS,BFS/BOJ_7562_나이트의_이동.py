from collections import deque

dxdys = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]

def solution(i,x1,y1,x2,y2):
    queue = deque()
    Map = [[-1 for _ in range(i)] for __ in range(i)]
    
    queue.append((x1,y1)) # x,y,count
    Map[y1][x1] = 0


    while len(queue) > 0:
        x,y = queue.popleft()

        for dxdy in dxdys:
            dx,dy = dxdy
            nx,ny = x + dx, y + dy
            if nx >= 0 and nx < i and ny >= 0 and ny < i:
                if Map[ny][nx] == -1:
                    Map[ny][nx] = Map[y][x] + 1
                    queue.append((nx,ny))

    return Map[y2][x2]

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