import sys

n = int(input())
mat = [list(map(int,list(sys.stdin.readline().rstrip()))) for _ in range(n)]
#왼쪽위 꼭지점이 x,y이고 한 변의 길이가 n인 정사각형을 처리

def search(y=0,x=0,l=n):
    bit = mat[y][x]

    isAllSame = 1
    for i in range(l):
        for j in range(l):
            if mat[y+i][x+j] != bit:
                isAllSame = 0
                break
        if isAllSame == 0:
            break
    
    if isAllSame:
        return str(bit)
    else:
        return "(" + search(y,x,l//2) + search(y,x+l//2,l//2) + search(y+l//2,x,l//2) + search(y+l//2, x+l//2,l//2) + ")"
    
print(search())