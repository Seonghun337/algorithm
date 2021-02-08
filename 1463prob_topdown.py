def solution(n):
    hist = [0] * 1000001
    hist[1] = 0

    return func(n,hist)

def func(n,hist):
    if n<=1:
        return 0
    if hist[n] != 0:
        return hist[n]

    hist[n] = func(n-1,hist) + 1
    if n % 3 == 0:
        hist[n] = min(hist[n],func(n//3,hist) + 1)
    if n % 2 == 0:
        hist[n] = min(hist[n],func(n//2,hist) + 1)

    return hist[n]


def main():
    n = int(input())
    print(solution(n))

main()