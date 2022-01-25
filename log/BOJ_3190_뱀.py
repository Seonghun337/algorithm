from collections import deque
n = int(input())
board = [[0 for _ in range(n)] for __ in range(n)]

k = int(input())
for _ in range(k):
    y,x = map(int,input().split())
    board[y-1][x-1] = 1

l = int(input())

moves = deque()
for _ in range(l):
    v,c = input().split()
    v = int(v)
    moves.append((v,c))

def show(board,i):
    print(str(i)+' ========')
    for line in board:
        print(*line)
    print()


dxdys = [(0,1),(1,0),(0,-1),(-1,0)]
direction = 0

snake = deque([(0,0)])
board[0][0] = -1

time = 0

v,c = moves.popleft()

while 1:
    time = time + 1

    y,x = snake[0]
    dy,dx = dxdys[direction]
    ny,nx = y + dy, x + dx
    if 0 <= ny < n and 0 <= nx < n:
        if board[ny][nx] == -1:
            # print('me')
            break
        else:
            if board[ny][nx] == 0:
                tail_y, tail_x = snake.pop()
                board[tail_y][tail_x] = 0

            snake.appendleft((ny,nx))
            board[ny][nx] = -1

    else:
        # print('wall-------')
        break
    


    if time == v:
        if c == 'D':
            direction = (direction + 1) % 4
        elif c == 'L':
            direction = (direction + 3) % 4
        
        if len(moves) > 0:
            v, c = moves.popleft()


    # show(board,time)

print(time)


