
n = int(input())

pivo = [1 for _ in range(n)]

for i in range(2,n):
    pivo[i] = pivo[i-1] + pivo[i-2]

print(pivo[n-1])