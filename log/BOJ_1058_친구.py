n = int(input())

adjMat = [list(map(int,list(input().replace('N','0').replace('Y','1')))) for _ in range(n)]

for i in range(n-1):
    for j in range(i+1,n):
        # 검사할 원소 (i,j)
        # i 노드에서 k 노드를 거쳐 j로 갈 수 있으면 업데이트
        if adjMat[i][j] == 0:
            for k in range(n):
                if adjMat[i][k] == 1 and adjMat[k][j] == 1:
                    adjMat[i][j] = 2
                    adjMat[j][i] = 2

# print(adjMat)

def count2friends(li):
    return n - li.count(0)

ans = []
for li in adjMat:
    ans.append(count2friends(li))
print(max(ans))