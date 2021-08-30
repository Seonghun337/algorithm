# i,j까지의 합을 모두 구해놓고
# 합집합 교집합 연산처럼

import sys

n,m = map(int,input().split())

mat = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

ops = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(m)]

dp = [[0 for _ in range(n)] for __ in range(n)]

# 일단 먼저 구해놓기
for i in range(n):
    if i == 0:
        dp[i][0] = mat[i][0]
    else:
        dp[i][0] = dp[i-1][0] + mat[i][0]

    for j in range(1,n):
        if i == 0:
            dp[i][j] = dp[i][j-1] + mat[i][j]
        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + mat[i][j]

# print(dp)
for xyxy in ops:
    x1,y1,x2,y2 = xyxy
    if x1 == 1 and y1 == 1:
        print(dp[x2-1][y2-1])
    elif x1 == 1 and y1 != 1:
        print(dp[x2-1][y2-1] - dp[x2-1][y1-2])
    elif y1 == 1 and x1 != 1:
        print(dp[x2-1][y2-1] - dp[x1-2][y2-1])
    else:
        print(dp[x2-1][y2-1] - dp[x1-2][y2-1] - dp[x2-1][y1-2] + dp[x1-2][y1-2])