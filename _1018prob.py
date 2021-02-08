w = 8
h = 8

def minPaint(matrix, y, x):
    cnt = 0
    chessMat = [[('W' if (j%2)^(i%2) == 0 else 'B') for j in range(w)] for i in range(h)]

    for i in range(h):
        for j in range(w):
            if matrix[y+i][x+j] == chessMat[i][j]:
                cnt = cnt+1
        
    return min(cnt, w*h - cnt)

def solve(n,m,matrix):
    minimum = w*h + 1

    for i in range(n-h+1):
        for j in range(m-w+1):
            minimum = min(minimum, minPaint(matrix, i, j))

    return minimum



def main():
    inputli = input().split(' ')
    n,m = int(inputli[0]),int(inputli[1])
    inputMatrix = []

    for i in range(n):
        inputMatrix.append(input())


    print(solve(n,m,inputMatrix))


main()