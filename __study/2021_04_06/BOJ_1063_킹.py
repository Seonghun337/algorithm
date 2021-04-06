#2021-04-06

dxdy = {'B':(1,0), 'T':(-1,0), 'R':(0,1), 'L':(0,-1), 'RT':(-1,1), 'LT':(-1,-1), 'RB':(1,1), 'LB':(1,-1)}
rows = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7}
rowsR = ['A','B','C','D','E','F','G','H']

def solution(K,S,N,moves):
    ky,kx = 8-int(K[1]), rows[K[0]]
    sy,sx = 8-int(S[1]), rows[S[0]]

    for move in moves:
        dy,dx = dxdy[move]
        ny,nx = ky+dy, kx+dx
        if ny >= 0 and ny < 8 and nx >= 0 and nx < 8:
            if ny == sy and nx == sx:
                nsy, nsx = sy + dy, sx + dx
                if nsy >= 0 and nsy < 8 and nsx >= 0 and nsx < 8:
                    ky,kx, sy,sx = ny,nx,nsy,nsx
                    # print(ky,kx,sy,sx)
                else:
                    continue
            else:
                ky,kx = ny,nx

    KR = rowsR[kx] + str(8-ky)
    SR = rowsR[sx] + str(8-sy)
    return KR,SR

def main():
    K, S, N = map(str,input().split())
    moves = []
    for _ in range(int(N)):
        moves.append(str(input()))
    
    resultK, resultS = solution(K,S,N,moves)
    print(resultK)
    print(resultS)

main()

