def solution(n,k,costs,rules,target):
    #rule을 선행조건으로 (순서 역으로)
    preconds = [[] for _ in range(n+1)]
    costs = [0] + costs

    for rule in rules:
        preconds[rule[1]].append(rule[0])

    hist = [-1 for _ in range(n+1)]
    a = cost(target,preconds,costs,hist)

    return a

def cost(target,preconds,costs,hist):
    if hist[target] != -1:
        return hist[target]

    if preconds[target]:
        maxCost = 0
        for precond in preconds[target]:
            c = cost(precond,preconds,costs,hist)
            if maxCost < c:
                maxCost = c

        hist[target] = maxCost + costs[target]
        return hist[target]
    else:
        return costs[target]


def main():
    T = int(input())
    answers = []
    for _ in range(T):
        n,k = map(int,input().split())
        costs = list(map(int,input().split()))
        rules = []
        for __ in range(k):
            a,b = map(int,input().split())
            rules.append((a,b))
        target = int(input())
        
        answers.append(solution(n,k,costs,rules,target))

    for answer in answers:
        print(answer)

main()