import sys

dd = [(x,y) for x in range(-1,2) for y in range(-1,2)]

def solution(n,m,mat1, mat2):
    cnt = 0
    for i in range(n):
        if i == 0 or i == n-1: continue
        for j in range(m):
            if j == 0 or j == m-1: continue
            if mat1[i-1][j-1] != mat2[i-1][j-1]:
                # print(i,j)
                cnt = cnt+1
                for d in dd:
                    dx,dy = d
                    mat1[i+dx][j+dy] = 1 if mat1[i+dx][j+dy]==0 else 0
                # print(mat1)

    for i in range(n):
        for j in range(m):
            if mat1[i][j] != mat2[i][j]:
                return -1

    return cnt


def main():
    n,m = map(int,input().split())
    matrix1 = []
    matrix2 = []
    for _ in range(n):
        matrix1.append(list(map(int,list(sys.stdin.readline().rstrip()))))

    for _ in range(n):
        matrix2.append(list(map(int,list(sys.stdin.readline().rstrip()))))

    print(solution(n,m,matrix1,matrix2))
    # print(d)

main()