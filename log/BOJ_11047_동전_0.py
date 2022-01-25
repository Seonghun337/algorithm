n, k = map(int,input().split())
coins = [int(input()) for _ in range(n)]

coins.reverse()

cnt = 0
for coin in coins:
    while k >= coin:
        cnt = cnt + (k//coin)
        k = k % coin
        

print(cnt)

#동전들이 배수라서 그냥 탐욕법