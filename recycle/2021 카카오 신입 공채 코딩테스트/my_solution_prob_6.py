# 누적 개념을 사용한다?
# 우측 하단 꼭지점에는 degree만큼 정연산(?) 해주고
# 좌측 상단 -1 꼭지점에는 degree만큼 역연산 해주면
# 25만개 다 돌고
# 마지막에 100만(1000*1000) 체크하면
# 시간 복잡도가 O(N*M + n(skill)) 이 된다
# 오케이, 가자

def solution(board, skill):
    n = len(board)
    m = len(board[0])
    
    accum_board = [[0] * (m+1) for _ in range(n+1)]
    coef = {1:-1, 2:1}

    for sk in skill:
        typ, y1, x1, y2, x2, degree = sk
        y1,x1,y2,x2 = y1+1,x1+1,y2+1,x2+1
        
        try:
            accum_board[y2][x2] += coef[typ]*degree
            accum_board[y1-1][x2] += (-1) * coef[typ]*degree
            accum_board[y2][x1-1] += (-1) * coef[typ]*degree
            accum_board[y1-1][x1-1] += coef[typ]*degree
        except:
            print(x1,y1,x2,y2)
            
    # prettyPrint(accum_board)
    answer = 0
    for i in range(n,-1,-1):
        for j in range(m,-1,-1):
            if i == n and j == m:
                accum_board[i][j] = accum_board[i][j]
            elif i == n:
                accum_board[i][j] = accum_board[i][j] + accum_board[i][j+1]
            elif j == m:
                accum_board[i][j] = accum_board[i][j] + accum_board[i+1][j]
            else:
                accum_board[i][j] = accum_board[i][j] + accum_board[i+1][j] + accum_board[i][j+1] - accum_board[i+1][j+1]
            
            if i != 0 and j != 0 and board[i-1][j-1] + accum_board[i][j] > 0:
                answer += 1
    
    # prettyPrint(board)
    # prettyPrint(accum_board)
    
    return answer

def prettyPrint(arr):
    print('>>>')
    for line in arr:
        for l in line:
            print(l, end='\t')
        print()