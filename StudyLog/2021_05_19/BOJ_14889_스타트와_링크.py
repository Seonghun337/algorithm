import sys
input = sys.stdin.readline

INF = int(1e9)
n = int(input().rstrip())
stats = [list(map(int,input().rstrip().split())) for _ in range(n)]

def getTeamStats(team, stats):
    sum_ = 0
    for player in team:
        for co_player in team:
            sum_ = sum_ + stats[player][co_player]
    return sum_

def search(home,n,k,stats):
    if len(home)==(n//2):
        away = [x for x in range(n) if x not in home]
        return abs(getTeamStats(home,stats)-getTeamStats(away,stats))
    elif n==k:
        return INF
    else:
        min_ = INF
        home.append(k)
        min_ = min(min_,search(home,n,k+1,stats))
        home.remove(k)
        min_ = min(min_,search(home,n,k+1,stats))
        return min_

print(search([0],n,1,stats))