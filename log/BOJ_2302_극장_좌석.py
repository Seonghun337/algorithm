# VIP를 넘어서서 자리가 바뀌는 경우는 없음 (두칸 건너야 되니까)
# 그러면 VIP를 기준으로 나눠서
# 각 부분 좌석에서 섞일 수 있는 경우의 수를 dp로 구하면 됨

# swap밖에 안됨
# 그 이상이면 두 칸 이상 이동이 반드시 필요함
# swap은 인접한 두 요소에 적용되고, 다른 swap과 영역이 겹칠 수 없음
# 따라서 i명이 앉는 경우의 수는
# i-2 번째까지 앉고 i-1과 i를 스왑하는 경우 + i-1까지 앉고 i번째에 그냥 앉는 경우

n = int(input())
m = int(input())
vips = [int(input()) for _ in range(m)] # 오름차순 정렬 되어있음


dp = [0 for _ in range(n+1)]
dp[0] = 1
dp[1] = 1 # dp[2] = 2 # 12, 21
for i in range(2,n+1):
    dp[i] = dp[i-2] + dp[i-1]

# 하고보니 피보나치?
answer = 1

prev = 0
for vip in vips:
    answer *= dp[vip - prev - 1]
    prev = vip
answer *= dp[n - prev]

# print(dp)
print(answer)