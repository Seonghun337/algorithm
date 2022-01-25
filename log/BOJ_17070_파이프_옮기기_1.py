# from collections import deque

# n = int(input())
# mat = [list(map(int,input().split())) for _ in range(n)]

# answer = 0

# # direction 0: 가로, 1: 대각선, 2: 세로
# dxdys = [ #(d,dx,dy)
#     [(0,1,0),(1,1,1)],
#     [(0,1,0),(1,1,1),(2,0,1)],
#     [(1,1,1),(2,0,1)]
# ]
# queue = deque([(0,0,1)]) # (d,y,x)
# while queue:
#     d,y,x = queue.popleft()

#     if x == n-1 and y == n-1:
#         answer += 1
#         continue

#     for dxdy in dxdys[d]:
#         dd,dx,dy = dxdy
#         nx,ny = x+dx, y+dy

#         if 0<=nx<n and 0<=ny<n and mat[ny][nx] == 0:
#             if dd == 1:
#                 if mat[y][x+1] == 0 and mat[y+1][x] == 0:
#                     queue.append((dd,ny,nx))
#             else:
#                 queue.append((dd,ny,nx))

# print(answer)
    

# n = int(input())
# mat = [list(map(int,input().split())) for _ in range(n)]

# answer = [[0]*n for _ in range(n)]
# answer[0][0] = 0
# answer[0][1] = 1

# for i in range(n):
#     for j in range(n):
#         if i==0 and j>=2:
#             if mat[i][j] == 0:
#                 answer[i][j] = answer[i][j-1]
#         elif i>=1 and j>=1:
#             print(i,j)
#             if mat[i][j] == 0:
#                 answer[i][j] += answer[i-1][j] + answer[i][j-1]
#                 if mat[i-1][j] == 0 and mat[i][j-1] == 0:
#                     answer[i][j] += answer[i-1][j-1]
#         elif j==0 and i>=1:
#             if mat[i][j] == 0:
#                 answer[i][j] = answer[i-1][j]

# print(answer)
# print(answer[-1][-1])

n = int(input())
mat = [list(map(int,input().split())) for _ in range(n)]

#0: 가로, 1: 대각선, 2: 세로
ans = [[[0]*n for _ in range(n)] for __ in range(3)]
ans[0][0][1] = 1
for j in range(2,n):
    if mat[0][j] == 0:
        ans[0][0][j] = ans[0][0][j-1]

for i in range(1,n):
    for j in range(1,n):
        if mat[i][j] == 0:
            ans[0][i][j] += ans[1][i][j-1]
            ans[0][i][j] += ans[0][i][j-1]

            ans[2][i][j] += ans[1][i-1][j]
            ans[2][i][j] += ans[2][i-1][j]

            if mat[i-1][j] == 0 and mat[i][j-1] == 0:
                ans[1][i][j] += ans[0][i-1][j-1] + ans[1][i-1][j-1] + ans[2][i-1][j-1]

# print(ans)
print(ans[0][-1][-1] + ans[1][-1][-1] + ans[2][-1][-1])