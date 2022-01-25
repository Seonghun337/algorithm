#21.02.04

import sys
input = sys.stdin.readline

n = int(input())
d = [[0]]

for _ in range(n):
    l = [0] + list(map(int,input().split()))
    d.append(l)

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            d[i][j] = d[i][j] | (d[i][k]&d[k][j])

for s in d[1:]:
    print(' '.join(map(str,s[1:])))