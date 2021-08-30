import sys
T = int(input())

for _ in range(T):
    n = int(input())
    chapters = list(map(int, sys.stdin.readline().rstrip().split()))

    # 딕셔너리에서 리스트로. i에서 j까지의 최소 비용
    cost = [[0]*n for _ in range(n)]

    
    for l in range(1,n): # 구간 길이
        for s in range(n-l): # 시작점
            e = s + l
            cost[s][e] = int(1e9)
            sum_ = sum(chapters[s:e+1]) # 현재 합치는 연산 때문에 생긴 비용
            for k in range(s, e): # 구분자
                cost[s][e] = min(cost[s][e], cost[s][k] + cost[k+1][e] + sum_)

    print(cost[0][n-1])

# 크누스 최적화...?