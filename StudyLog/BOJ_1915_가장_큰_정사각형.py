n,m = map(int,input().split())

mat = [list(map(int,list(input()))) for _ in range(n)]

# 위,왼위,왼 중 가장 작은 값 + 1
for i in range(1,n):
    for j in range(1,m):
        if mat[i][j] == 1:
            mat[i][j] = min(mat[i-1][j], mat[i-1][j-1], mat[i][j-1]) + 1

# 최대 값 찾으면 됨
ans = []
for li in mat:
    ans.append(max(li))

print(max(ans)**2)