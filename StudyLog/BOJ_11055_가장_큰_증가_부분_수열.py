import sys
n = int(input())
line = list(map(int,sys.stdin.readline().rstrip().split()))

dp = [0 for _ in range(n)]

for i in range(len(line)):

    M = 0
    for j in range(i):
        if line[j] < line[i]:
            M = max(M,dp[j])
    
    dp[i] = M + line[i]


print(max(dp))
