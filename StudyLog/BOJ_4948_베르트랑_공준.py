primes = [2]
MAX = 246912
estenetos = [0 for _ in range(MAX)]

for x in range(3, MAX, 2):
    if estenetos[x] == 1:
        continue
    else:
        primes.append(x)
        i = 2
        while x*i < MAX:
            estenetos[x*i] = 1
            i = i + 1

buf = []
while 1:
    n = int(input())
    if n==0:
        break
    buf.append(len([x for x in primes if x > n and x <= 2*n]))
    
for a in buf:
    print(a)