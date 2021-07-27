f,s,g,u,d = map(int,input().split())
cnt = 0

visited = {}

strImpossible = 'use the stairs'

from collections import deque
queue = deque()

queue.append((s,0))
visited[s] = 1

while queue:
    now, degree = queue.popleft()

    if now==g:
        print(degree)
        break
    if now + u <= f:
        if (now+u) not in visited:
            queue.append((now+u, degree+1))
            visited[now+u] = 1

    if now - d >= 1:
        if (now-d) not in visited:
            queue.append((now-d, degree+1))
            visited[now-d] = 1
else:
    print(strImpossible)


# 그리디 안됨
# 당연히
#
# while 1:
#     # print(s,cnt,visited)
#     if s == g:
#         print(cnt)
#         break
#     elif s < g:
#         if s+u > f+d:
#             break
#         s = s + u
#         if s in visited:
#             print(strImpossible)
#             break
#         else:
#             visited[s] = 1
#         cnt = cnt + 1

#     elif s > g:
#         s = s - d
#         if s in visited:
#             print(strImpossible)
#             break
#         else:
#             visited[s] = 1
#         cnt = cnt + 1

    
    
