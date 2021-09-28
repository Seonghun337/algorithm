# 플로이드 워셜
# 갈 수 있다, 없다만 체크

def getDistance(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)

T = int(input())

for _ in range(T):
    n = int(input())
    
    nodes = [None for _ in range(n+2)]
    mat = [[0] * (n+2) for _ in range(n+2)]

    for i in range(n+2):
        x,y = map(int,input().split())

        for j in range(i):
            std_x, std_y = nodes[j]
            if getDistance(x,y,std_x,std_y) <= 1000:
                mat[i][j] = 1
                mat[j][i] = 1

        nodes[i] = (x,y)

    # print(mat)
    # 플로이드 워셜
    for k in range(n+2):
        for i in range(n+2):
            for j in range(n+2):
                if mat[i][k] == 1 and mat[k][j] == 1:
                    mat[i][j] = 1
                    
    # print('after')
    # print(mat)
    if mat[0][-1] == 1:
        print("happy")
    else:
        print("sad")


    
