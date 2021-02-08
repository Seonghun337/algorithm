
def solution(n,m,r,c,d,mat):
    cnt = 0
    x = c
    y = r
    di = d
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    while True:
        if mat[y][x] == 0:
            mat[y][x] = 2    #현재 위치 청소
            cnt = cnt + 1

        nextdi = (di + 3) % 4    #왼쪽으로 회전
        if mat[y + dy[nextdi]][ x + dx[nextdi]] == 0:
            di = nextdi
            x = x + dx[di]
            y = y + dy[di]
        else:
            if mat[y+dy[0]][x+dx[0]] != 0 and mat[y+dy[1]][x+dx[1]] != 0 and mat[y+dy[2]][x+dx[2]] != 0 and mat[y+dy[3]][x+dx[3]] != 0:
                if mat[y - dy[di]][x - dx[di]] == 1:
                    break
                else:
                    x = x - dx[di]
                    y = y - dy[di]
            else:
                di = nextdi

    return cnt


def main():
    n, m = map(int,input().split())
    r,c,d = map(int,input().split())
    mat = []
    for i in range(n):
        mat.append(list(map(int,input().split())))

    print(solution(n,m,r,c,d,mat))


main()