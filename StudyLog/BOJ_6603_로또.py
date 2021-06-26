from itertools import combinations
import sys

inputs = []

while 1:
    S = list(map(int,sys.stdin.readline().rstrip().split()))
    if S[0] == 0:
        break
    inputs.append(S)

for S in inputs:
    exc = list(combinations(S[1:],S[0]-6))
    n = S[0]
    line = S[1:]
    exc.reverse()
    for e in exc:
        print(*[line[i] for i in range(n) if line[i] not in e])
    
    print()