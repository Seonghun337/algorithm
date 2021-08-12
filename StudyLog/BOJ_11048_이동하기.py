n,m = map(int,input().split())

mat = [list(map(int,input().split())) for _ in range(n)]

for j in range(1,m):
    mat[0][j] = mat[0][j-1] + mat[0][j]

for i in range(1,n):
    mat[i][0] = mat[i-1][0] + mat[i][0]
    for j in range(1,m):
        mat[i][j] = max(mat[i-1][j], mat[i-1][j-1], mat[i][j-1]) + mat[i][j]

print(mat[-1][-1])