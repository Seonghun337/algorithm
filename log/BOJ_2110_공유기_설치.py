# 모르겠어서 찾아봄
# 설치 가능을 판단하는 함수를 작성하고
# 그걸로 이분 탐색

n,c = map(int,input().split())
nodes = [int(input()) for _ in range(n)]
nodes.sort()

def howManyPossible(min_dist):

    cnt = 1
    prev_x = nodes[0]
    prev_dist = 0
    for i in range(1,len(nodes)):
        # print(nodes[i],prev_x,prev_dist, nodes[i]-prev_x+prev_dist)
        dist = prev_dist + nodes[i] - prev_x
        if dist >= min_dist:
            prev_dist = 0
            cnt = cnt + 1
        else:
            prev_dist = dist
        prev_x = nodes[i]

    return cnt

ans = 0

a = 1 # 나올 수 있는 거리의 최솟값
b = nodes[-1] - nodes[0] # 나올 수 있는 거리의 최댓값

while a <= b:
    mid = (a+b) // 2


    if howManyPossible(mid) >= c:
        # print(a,b,str(mid) + ' is poss')
        ans = mid
        a = mid+1
    else:
        # print(a,b,str(mid) + ' is imposs')
        b = mid-1



print(ans)

# print(howManyPossible(4))