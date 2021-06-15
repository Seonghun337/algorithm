n,k = map(int,input().split())

from collections import deque

array = [-1 for _ in range(100001)]
array[n] = 0

queue = deque()
queue.append((n,0))

while array[k] == -1:
    now, time = queue.popleft()
    
    nexts = [now+1,now-1,now*2]
    for next in nexts:
        if 0<=next<=100000 and array[next] == -1:
            queue.append((next,time+1))
            array[next] = time+1

print(array[k])

