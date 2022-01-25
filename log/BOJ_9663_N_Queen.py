n = int(input())

# 행 하나에 퀸 하나씩

# 열 같으면 안되고
# 행차이 절댓값 = 열차이 절댓값 이면, 대각선에 있음

cnt = 0
board = [-1 for _ in range(n)]

def search(n, i = 0):
    global cnt
    global board
    if i == n:
        # print(board)
        cnt = cnt + 1
    
    # sum = 0
    for j in range(n):

        # 다 통과하면 j에 놓일 수 있음
        isOk = 1
        for k in range(i):
            if board[k] == j or abs(i-k) == abs(j-board[k]):
                isOk = 0
                break
                
        if isOk:
            board[i] = j
            search(n, i+1)



search(n)
print(cnt)