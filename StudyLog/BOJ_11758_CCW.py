x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
x3,y3 = map(int,input().split())

# P2->P1, P2->P3 두 벡터를 만들어서 외적(두 벡터가 포함된 평면의 수직인 벡터)결과가
# 오른손 법칙으로 나옴

v1 = (x1-x2, y1-y2, 0)
v2 = (x3-x2, y3-y2, 0)

# 모르겠다
z = (x2-x1)*(y3-y1) - (x3-x1)*(y2-y1)

if z==0:
    print(0)
else:
    print(z//abs(z))