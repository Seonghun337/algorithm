# 시간초과....ㄹㅇ
# PyPy3로 통과했지만 시간 더 줄여보기
n = int(input())


dp = [0] * (n+1)
dp[1] = 1
for x in range(2,n+1):
    # dp.append(x)
    dp[x] = x
    for j in range(2,x):
        if x - j*j >= 0:
            dp[x] = min(dp[x-j*j] + 1, dp[x])
        else:
            break

print(dp[n])