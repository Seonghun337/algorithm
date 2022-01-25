import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
inputs = []
for _ in range(T):
    n,m = map(int,input().rstrip().split())
    line = input().rstrip().split()
    queue = deque()
    for i in range(len(line)):
        queue.append((int(line[i])))

    inputs.append((n,m,queue))

# for I in inputs:
#     n,m,queue = I
#     cnt = 0
#     while 1:
#         w, i = queue.popleft()
#         if w == max(queue)

for I in inputs:
    n,m,queue = I
    targetIdx = m
    answer = 0
    while queue:
        if queue[0] == max(queue):
            # print(queue,targetIdx)
            answer = answer + 1
            if targetIdx == 0:
                break 
            else:
                del queue[0]
        else:
            tmp= queue[0]
            del queue[0]
            queue.append(tmp)
        l = len(queue)
        targetIdx = (targetIdx + l - 1) % l

    print(answer)