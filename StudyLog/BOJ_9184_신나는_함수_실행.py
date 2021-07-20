inputs = []

while 1:
    a, b, c = map(int,input().split())
    if a==b==c==-1:
        break
    else:
        inputs.append((a,b,c))

dp = {}

def w(a,b,c):
    if (a,b,c) in dp:
        return dp[(a,b,c)]

    if a <= 0 or b <= 0 or c <= 0:
        dp[(a,b,c)] = 1
        return 1

    if a > 20 or b > 20 or c > 20:
        result = w(20, 20, 20)
        dp[(a,b,c)] = result
        return result

    if a < b and b < c:
        result = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        dp[(a,b,c)] = result
        return result

    result = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    dp[(a,b,c)] = result
    return result

for i in inputs:
    a,b,c = i
    print(f'w({a}, {b}, {c}) = {w(a,b,c)}')