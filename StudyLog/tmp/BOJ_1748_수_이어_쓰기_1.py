n = int(input())

cnt = 0
nDigit = len(str(n))
for i in range(1,nDigit):
    cnt = cnt + 9 * (10 ** (i-1)) * i

cnt = cnt + nDigit * (n - 10**(nDigit-1) + 1)
print(cnt)