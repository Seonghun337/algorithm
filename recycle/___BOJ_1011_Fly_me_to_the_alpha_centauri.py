from collections import deque

T = int(input())

inputs = []

for _ in range(T):
    x,y = map(int,input().split())
    inputs.append((x,y))

for inp in inputs:
    x, y = inp

    visited = set()
    queue = deque([(0,y)])

    while queue:
        d,k = queue.popleft()
        if k == x:
            break
        for w in [-1,0,1]:
            if k+w > 0:
                queue.append((d+1,k+w))
    print(k)
        