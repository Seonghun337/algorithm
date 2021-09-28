# 에라토스테네스 이후 투포인터

n = int(input())

primes = [] # 투포인터 할 것이기 때문에 인덱스로 접근할 수 있는 리스트에 담음

numbers = [0 for _ in range(n+1)]
for i in range(2, n+1):
    if numbers[i] == 0:
        primes.append(i)
        k = 2
        while k*i <= n:
            numbers[k*i] = 1
            k = k+1


m = len(primes)
answer = 0
a = 0
b = 0
sum = 0
if n != 1:
    sum = primes[0]

while a <= b and b < m:
    # print(a,b,sum)
    if sum == n:
        answer += 1
        if b != m-1:
            b += 1
            sum += primes[b]
        else:
            break
    elif sum < n: # 커져야됨
        if b != m-1:
            b += 1
            sum += primes[b]
        else:
            break
    else: # 작아져야됨
        sum -= primes[a]
        a += 1


print(answer)

    