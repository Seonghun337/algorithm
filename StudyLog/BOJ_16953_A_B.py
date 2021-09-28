from collections import deque

a,b = map(int,input().split())


# 두 연산 모두 현재 수를 증가시키는 연산이므로
# 큐에서 뽑은 수가 b보다 크다면 무시하고 넘어간다.
# b가 되기 전에 큐가 비워지면 b를 만들 수 없는 경우이다.


visited = set()
queue = deque()
visited.add(a)
queue.append((1,a))

while queue:
    w,now = queue.popleft()

    if now == b:
        print(w)
        break
    elif now < b:
        new1 = now*10 + 1
        new2 = now*2

        if new1 not in visited:
            queue.append((w+1,new1))
            visited.add(new1)

        if new2 not in visited:
            queue.append((w+1,new2))
            visited.add(new2)

    # print(queue)
else:
    print(-1)