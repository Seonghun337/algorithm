n = int(input())
nodes = list(map(int,input().split()))
target = int(input())


isLeaf = [0]*n


# 유니온 파인드
for x in range(n):
    if isLeaf[x] == 0 and x != target:
        isLeaf[x] = 1

        now = x
        while True:
            now = nodes[now]
            if now == target:
                isLeaf[x] = -1
            if now == -1:
                break
            else:
                isLeaf[now] = -1

answer = sum([x for x in isLeaf if x == 1])
print(answer)