import heapq

INF = int(1e9)

def solution(n,m,mat):
    d = [[INF for _ in range(m)] for j in range(n)]
    visited = [[0 for _ in range(m)] for j in range(n)]
    

    queue = []

    y,x = 0,0

    heapq.heappush(queue,(mat[y][x],y,x))
    d[y][x] = mat[y][x]

    while len(queue) > 0:
        w,y1,x1 = heapq.heappop(queue)
        

        if visited[y1][x1]:
            continue

        visited[y1][x1] = 1

        if y1+1 < n :
            d[y1+1][x1] = min(d[y1+1][x1],d[y1][x1] + mat[y1+1][x1])
            heapq.heappush(queue,(d[y1+1][x1],y1+1,x1))

        if y1-1 >= 0 :
            d[y1-1][x1] = min(d[y1-1][x1],d[y1][x1] + mat[y1-1][x1])
            heapq.heappush(queue,(d[y1-1][x1],y1-1,x1))

        if x1+1 < m :
            d[y1][x1+1] = min(d[y1][x1+1],d[y1][x1] + mat[y1][x1+1])
            heapq.heappush(queue,(d[y1][x1+1],y1,x1+1))

        if x1-1 >= 0:
            d[y1][x1-1] = min(d[y1][x1-1], d[y1][x1] + mat[y1][x1-1])
            heapq.heappush(queue,(d[y1][x1-1],y1,x1-1))

        


    return d[n-1][m-1]

    


def main():
    m,n = map(int,input().split())
    mat = []
    for _ in range(n):
        mat.append(list(map(int,list(input()))))

    print(solution(n,m,mat))

main()