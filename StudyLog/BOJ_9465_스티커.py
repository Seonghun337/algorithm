def solution(n, line):
    if n == 1:
        print(max(line[0][0],line[1][0]))
        return

    dp = [[0 for _ in range(n)],[0 for _ in range(n)]]
    dp[0][0] = line[0][0]
    dp[1][0] = line[1][0]
    dp[0][1] = dp[1][0] + line[0][1]
    dp[1][1] = dp[0][0] + line[1][1]

    for i in range(2,n):
        dp[0][i] = max(dp[1][i-2]+line[0][i], dp[0][i-2] + line[0][i], dp[1][i-1] + line[0][i])
        dp[1][i] = max(dp[0][i-2]+line[1][i], dp[1][i-2] + line[1][i], dp[0][i-1] + line[1][i])

    print(max(dp[0][-1],dp[1][-1]))



T = int(input())
import sys
inputs = []
for _ in range(T):
    n = int(input())
    line = [list(map(int,sys.stdin.readline().rstrip().split())), list(map(int,sys.stdin.readline().rstrip().split()))]
    inputs.append((n,line))

for i in inputs:
    n,line = i
    solution(n,line)
    

