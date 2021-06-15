#2021-04-06

def solution(x):
    # sticks = [64]
    cnt = 1
    Sum = 64
    shortestStick = 64
    while Sum > x:
        cut = shortestStick // 2
        if Sum - cut >= x:
            Sum = Sum - cut
        else:
            cnt = cnt + 1
        shortestStick = cut

        # print(Sum,shortestStick)

    return cnt

def main():
    x = int(input())
    print(solution(x))

main()