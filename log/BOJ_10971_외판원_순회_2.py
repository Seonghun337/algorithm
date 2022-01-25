import sys

n = int(input())

adjarr = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

from itertools import permutations

cases = permutations(range(1,n+1),n)

_min = int(1e9)
for c in cases:
    c = c + c[0:1]
    sum_ = 0
    isNotOk = 0
    for i in range(n):
        w = adjarr[c[i]-1][c[i+1]-1]
        if w == 0:
            isNotOk = 1
            break
        else:
            sum_ = sum_ + w
            if sum_ > _min:
                isNotOk = 1
                break
    if isNotOk == 0 and sum_ < _min:
        _min = sum_
    # print(c,sum_)

print(_min)