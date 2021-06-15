n = int(input())
num = 1
arr = [int(input()) for _ in range(n)]
stack = []
result = []


for target in arr:
    while 1:
        if len(stack)>0 and stack[-1] == target:
            result.append('-')
            stack.pop()
            break
        else:
            if num <= n:
                result.append('+')
                stack.append(num)
                num = num + 1
            else:
                break


if stack:
    print('NO')
else:
    for y in result:
        print(y)