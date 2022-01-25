# 1 1 1 1 1
# 1 2 3 4 5
# 1 3 6 10 15

n,m,k = map(int,input().split())

# 동그라미의 위치를 좌표로 변환
k_y = 0
k_x = 0
if k != 0:
    k_y = (k-1) // m
    k_x = (k-1) % m

    # 구해야 되는 경우의 수의 최댓값을 구하기
max_y = max(k_y,n)
max_x = max(k_x,m)

dp = [[1] * max_x for _ in range(max_y)]

for i in range(1,max_y):
    for j in range(1,max_x):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

# print(dp)

if k == 0:
    print(dp[-1][-1])
else:
    # print('k',k_y,k_x)
    # print('else',n-k_y,m-k_x)
    print(dp[k_y][k_x] * dp[n-k_y-1][m-k_x-1])