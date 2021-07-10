import sys

T = int(input())
answer = []


def solution(n,nums):
    cnt = 0
    visited = [-1 for _ in range(n+1)]
    for start in range(1,n+1):
        if visited[start] == -1:
            cnt = cnt + 1
            now = start
            while 1:
                if visited[now] == 0:
                    break
                else:
                    visited[now] = 0
                    now = nums[now]
                
    return cnt

for _ in range(T):
    n = int(input())
    nums = [-100] + list(map(int,sys.stdin.readline().rstrip().split()))
    answer.append(solution(n,nums))

for x in answer:
    print(x)


