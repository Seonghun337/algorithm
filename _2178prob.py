from collections import deque

INF = 9999

def solution(n,m,mat):
    result = [[INF for __ in range(m)] for _ in range(n)]
    visited = [[0 for __ in range(m)] for _ in range(n)]
    queue = deque()

    queue.append((0,0))
    result[0][0] = 1
    
    while True:
        if len(queue)==0:
            break

        cy,cx = queue.popleft()
        visited[cy][cx] = 1

        if cy+1 < n and mat[cy+1][cx] == 1 and visited[cy+1][cx] == 0:
            queue.append((cy+1,cx))
            visited[cy+1][cx] = 1
            result[cy+1][cx] = min(result[cy+1][cx],result[cy][cx]+1)
        
        if cx+1 < m and mat[cy][cx+1] == 1 and visited[cy][cx+1] == 0:
            queue.append((cy,cx+1))
            visited[cy][cx+1] = 1
            result[cy][cx+1] = min(result[cy][cx+1],result[cy][cx]+1)   

        if cy-1 >= 0 and mat[cy-1][cx] == 1 and visited[cy-1][cx] == 0:
            queue.append((cy-1,cx))
            visited[cy-1][cx] = 1
            result[cy-1][cx] = min(result[cy-1][cx],result[cy][cx]+1)   

        if cx-1 >= 0 and mat[cy][cx-1] == 1 and visited[cy][cx-1] == 0:
            queue.append((cy,cx-1))
            visited[cy][cx-1] = 1
            result[cy][cx-1] = min(result[cy][cx-1],result[cy][cx]+1)  


    return result[-1][-1]


def main():
    n, m = map(int,input().split())
    mat = []
    for _ in range(n):
        mat.append(list(map(int,input())))

    print(solution(n,m,mat))

main()