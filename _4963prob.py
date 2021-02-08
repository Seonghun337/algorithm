from collections import deque

def solution(n,m,mat):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 1:
                fill(n,m,i,j,mat)
                cnt = cnt + 1
    return cnt


def fill(n,m,y,x,mat):
    queue = deque()
    queue.append((y,x))

    while len(queue) > 0:
        (i,j) = queue.popleft()
        mat[i][j] = 0

        if i+1 < n and mat[i+1][j] == 1:
            queue.append((i+1,j))
            mat[i+1][j] = 0
        if i-1 >= 0 and mat[i-1][j] == 1:
            queue.append((i-1,j))
            mat[i-1][j] = 0
        if j+1 < m and mat[i][j+1] == 1:
            queue.append((i,j+1))
            mat[i][j+1] = 0
        if j-1 >= 0 and mat[i][j-1] == 1:
            queue.append((i,j-1))
            mat[i][j-1] = 0
        if i+1 < n and j+1 < m and mat[i+1][j+1] == 1:
            queue.append((i+1,j+1))
            mat[i+1][j+1] = 0
        if i-1 >= 0 and j+1 < m and mat[i-1][j+1] == 1:
            queue.append((i-1,j+1))
            mat[i-1][j+1] = 0
        if j-1 >= 0 and i-1 >= 0 and mat[i-1][j-1] == 1:
            queue.append((i-1,j-1))
            mat[i-1][j-1] = 0
        if j-1 >= 0 and i+1 < n and mat[i+1][j-1] == 1:
            queue.append((i+1,j-1))
            mat[i+1][j-1] = 0

def main():
    inputList = []
    while True:
        w,h = map(int,input().split())

        if w==0 and h==0:
            break

        mat = []
        for i in range(h):
            mat.append(list(map(int,input().split())))

        inputList.append((w,h,mat))

    for inputRow in inputList:
        print(solution(inputRow[1],inputRow[0],inputRow[2]))


main()