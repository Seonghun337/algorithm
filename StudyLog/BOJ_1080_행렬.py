n,m = map(int,input().split())

mat1 = [list(map(int,list(input()))) for _ in range(n)]
mat2 = [list(map(int,list(input()))) for _ in range(n)]
cnt = 0
if n >= 3 and m >= 3:
    for i in range(1,n-1):
        for j in range(1,m-1):
            if mat1[i-1][j-1] != mat2[i-1][j-1]:
                cnt = cnt + 1

                #변환
                for k in range(3):
                    for l in range(3):
                        if mat1[i-1+k][j-1+l] == 1:
                            mat1[i-1+k][j-1+l] = 0
                        else:
                            mat1[i-1+k][j-1+l] = 1
        

isOk = 1
for i in range(n):
    for j in range(m):
        if mat1[i][j] != mat2[i][j]:
            isOk = 0
            break
    if isOk == 0:
        break

if isOk:
    print(cnt)
else:
    print(-1)