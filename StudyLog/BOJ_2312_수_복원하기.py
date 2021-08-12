T = int(input())
inputs = [int(input()) for _ in range(T)]

maxN = 100001
astenetos = [-1 for _ in range(maxN)]
primes = []

for i in range(2,maxN):
    if astenetos[i] == -1:
        primes.append(i)
        j = 2
        while 1:
            if i*j < maxN-1:
                astenetos[i*j] = 0
            else:
                break
            j = j + 1

def decompose(n):
    global primes
    # primeIdx = 0

    for i in range(len(primes)):
        cnt = 0
        while n % primes[i] == 0:
            n = n // primes[i]
            cnt = cnt + 1
        if cnt != 0:
            print(primes[i],cnt)
        if n == 1:
            break
    



for inp in inputs:
    decompose(inp)





