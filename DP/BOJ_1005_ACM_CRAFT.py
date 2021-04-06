import sys
from collections import deque

def cost(n,rules,costs,hist):
    if hist[n] != -1:
        return hist[n]
    
    if len(rules[n]) == 1:
        return costs[n-1]

    maxCost = -1
    # print(rules[n][1:])
    for rule in rules[n][1:]:
        c = cost(rule,rules,costs,hist)
        if maxCost < c:
            maxCost = c

    # print(hist)
    hist[n] = maxCost + costs[n-1]
    return (maxCost + costs[n-1])


# def solution(n,k,costs,rules,target):
#     hist = [-1 for _ in range(n+1)]
#     # print(rules)
#     return cost(target,rules,costs,hist)

def solution(n,k,costs,rules,target):
    hist = [-1 for _ in range(n+1)]
    visited = [-1 for _ in range(n+1)]
    # queue = deque()
    stack = []
    
    # queue.append(target)
    stack.append(target)

    while len(stack)>0:
        currentNode = stack[-1]
        if visited[currentNode] == -1:
            if len(rules[currentNode]) == 1:
                hist[currentNode] = costs[currentNode-1]
                stack.pop()
            else:
                for rule in rules[currentNode][1:]:
                    stack.append(rule)
            visited[currentNode] = 0
        else:
            if len(rules[currentNode]) == 1:
                stack.pop()
            else:
                maxCost = -1
                for rule in rules[currentNode][1:]:
                    if maxCost < hist[rule]:
                        maxCost = hist[rule]
                maxCost = maxCost + costs[currentNode-1]
                hist[currentNode] = maxCost
                stack.pop()

    return hist[target]
    


def main():
    T = int(input())
    inputs = []
    for _ in range(T):
        n,k = map(int,input().split())
        costs = list(map(int,sys.stdin.readline().rstrip().split()))
        rules = [[0] for i in range(n+1)]


        for __ in range(k):
            a,b = map(int,sys.stdin.readline().rstrip().split())
            rules[b].append(a)
        target = int(input())
        
        inputs.append((n,k,costs,rules,target))


    for inpt in inputs:
        n,k,costs,rules,target = inpt
        print(solution(n,k,costs,rules,target))

main()


# 첫 번째 시도 : DP로 풀었으나 시간 초과
# 두 번째 시도 : 입력을 readline으로 바꾸니 엄청 빨라짐// input 방법 중요!!
# 세 번째 시도 : input이 너무 커서 recursion 에러인것 같음
# recursion to loop