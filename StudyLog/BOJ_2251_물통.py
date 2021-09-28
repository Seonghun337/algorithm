# 첫번째 물통이 비어있을 때, 세번째 물통에 담겨있을 수 있는 물의 양?
# 8 9 10
# 1 - 0 9 1
# 2 - 0 8 2     # A에 부었다가 B에 부으면 B에 8 담겨있음
# 8 - 0 2 8

# 세 물통의 용량에 따라 만들 수 있는 물의 양이 다양하게 변하는 것 같ㅌ음(규칙이 없음)
# 따라서, 물을 계속 옮겨가며 만들 수 있는 물의 양을 저장
# A가 비어있는 경우만 생각하므로 B또는 C에 들어있는 물의 양을 알면 한 가지 경우의 수를 결정할 수 있음
# 종료조건은 담길 수 없는 물인지를 검사

# 각 단계에서 취할 수 있는 행동은
# a -> b, a -> c, b -> a, b -> c, c -> a, c -> b
# 상하좌우 이동을 dxdy로 나타냈던 것처럼 from to로 나타냄

from collections import deque

a,b,c = map(int,input().split())

# 각 물통을 인덱스로 접근해서 사용할 수 있도록 (a:0, b:1, c:2)
capacity = (a,b,c)
fromto = [(0,1),(0,2),(1,0),(1,2),(2,0),(2,1)]

answer = set() # c에 담겨있을 수 있는 물의 양
answer.add(c)

queue = deque()
queue.append((0,0,c))
visited = set()
visited.add((0,0,c))

while queue:
    now = queue.popleft()
    for ft in fromto:
        f,t = ft
        new = list(now)
        new[t] = min(now[t] + now[f], capacity[t])
        new[f] = max(now[f] - capacity[t] + now[t], 0) # 헷갈림


        if tuple(new) not in visited:
            visited.add(tuple(new))
            queue.append(tuple(new))

            if new[0] == 0:
                answer.add(new[2])

print(*sorted(list(answer)))