#21.02.03

def solve(n):
    hist = {0:(1,0), 1:(0,1)}
    f = fibo(n, hist)
    return ' '.join(list(map(str,f)))

def fibo(n, hist):
    if n == 0:
        return (1, 0)
    elif n == 1:
        return (0, 1)
    else:
        if n in hist:
            return hist[n]
        else:
            f = sum(fibo(n-1,hist),fibo(n-2,hist))
            hist[n] = f
            return f

def sum(a,b):
    return (a[0]+b[0],a[1]+b[1])

def main():
    T = int(input())
    inputList = []
    for i in range(T):
        inputList.append(int(input()))

    for i in range(T):
        print(solve(inputList[i]))


main()


# 재귀함수 + 동적계획법
# int : tuble dictionary
# (0호출횟수, 1호출횟수)
# 한 번 계산한 것은 다시 계산 안하도록