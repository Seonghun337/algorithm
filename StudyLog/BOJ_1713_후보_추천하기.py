# 이거 운영체제가 스케쥴링 하는 알고리즘인데
# RL뭐시기

import sys

n = int(input())
m = int(input())
voteArr = list(map(int,sys.stdin.readline().rstrip().split()))

import heapq

table = []
order = []

cnt = 0

for vote in voteArr:
    cnt = cnt + 1

    if vote in table:
        i = table.index(vote)
        v, c = order[i]
        order[i] = (v+1, c)
        continue

    if len(table) < n:
        table.append(vote)
        order.append((1, cnt))
    else:
        i = order.index(min(order))
        table[i] = vote
        order[i] = (1, cnt)



print(*sorted(table))


