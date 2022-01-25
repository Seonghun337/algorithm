n = int(input()) 
polys = [tuple(map(int,input().split())) for _ in range(n)]
polys.sort()

def getMaxHeightIndex(polys,a,b):
    idx = 0
    Maxheight = -1
    for i in range(a,b):
        h = polys[i][1]
        if Maxheight < h:
            Maxheight = h
            idx = i
    return idx

# 왼쪽 파트가 -1, 오른쪽 파트가 1, 루트가 0
# a:b 사이의 넓이를 리턴
def search(polys,a=0,b=n,direction=0):
    i = getMaxHeightIndex(polys,a,b) #최대 높이인 막대의 인덱스 구하기 O(n)
    if direction==0:
        S = 0
        if i > 0:
            S = S + search(polys,a,i,-1)
        if i < n-1:
            S = S + search(polys,i+1,b,1)
        return polys[i][1] + S
    elif direction==-1:
        S = (polys[b][0] - polys[i][0]) * polys[i][1] # 오른쪽 부분 넓이
        if i > 0:
            S = S + search(polys, a, i, -1)
        return S
    elif direction==1:
        S = (polys[i][0] - polys[a-1][0]) * polys[i][1] # 왼쪽 부분 넓이
        if i < n-1:
            S = S + search(polys, i+1, b, 1)
        return S
        

print(search(polys))
