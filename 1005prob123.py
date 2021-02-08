def solution(n,k,costs,preconds,target):

    costs = [0] + costs
    hist = {}

    return cost(target,preconds,costs,hist)
    
def cost(target,preconds,costs,hist):
    if hist.get(target) != None:
        return hist[target]


    if len(preconds[target]):
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
        rules = [[] for _ in range(n+1)]
        for __ in range(k):
            a,b = map(int,input().split())
            rules[b].append(a)
        target = int(input())
        
        answers.append(solution(n,k,costs,rules,target))

    for answer in answers:
        print(answer)

main()