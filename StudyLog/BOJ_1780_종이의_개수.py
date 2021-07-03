import sys

n = int(input())

board = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

cnt = [0,0,0]

def search(board, n, y=0, x=0):
    global cnt

    #terminate condition

    val = board[y][x]
    for i in range(n):
        for j in range(n):
            if val != board[y+i][x+j]:
                #잘라야됨
                for k in range(3):
                    for l in range(3):
                        search(board,n//3,y + k*n//3, x + l*n//3)
                return

    cnt[val+1] += 1


search(board,n)

for c in cnt:
    print(c)