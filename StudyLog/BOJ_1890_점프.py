import sys

n = int(input())

board = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

count = [[0 for _ in range(n)] for __ in range(n)]

for i in range(n-1,-1,-1):
    for j in range(n-1,-1,-1):
        if i == n-1 and j == n-1:
            count[i][j] = 1
            continue

        distance = board[i][j]

        if i + distance < n:
            count[i][j] = count[i][j] + count[i+distance][j]
        
        if j + distance < n:
            count[i][j] = count[i][j] + count[i][j+distance]

        
# print(count)
# print(board)
print(count[0][0])