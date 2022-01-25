from collections import defaultdict

T = int(input())
result = []
for _ in range(T):
    n = int(input())
    dic = defaultdict(list)
    for _ in range(n):
        name, type = input().split()
        dic[type].append(name)
    cnt = 1
    for key in dic:
        cnt = cnt * (len(dic[key]) + 1)
    
    cnt = cnt - 1

    result.append(cnt)

for r in result:
    print(r)
