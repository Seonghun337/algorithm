n = int(input())
m = int(input())

# 1이면 나보다 무거운거, 2이면 나보다 가벼운거 # 나 = 행번호
mat = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    mat[a][b] = 2
    mat[b][a] = 1


for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if mat[i][k] == mat[k][j] and mat[i][k] != 0:
                mat[i][j] = mat[i][k]


for i in range(1,n+1):
    print(n-1-sum([1 for x in mat[i] if x == 1 or x == 2]))