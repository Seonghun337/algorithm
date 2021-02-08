# 무게 추 하나씩 검사 (작은 것부터)
# maxN = k번 째 무게추까지 사용하여 만들수 있는 무게 중 최댓값 (연속해서)
# 추를 모두 사용한 숫자까지 연속일 경우를 위해 마지막에 maxN+1
def solution(n,weights):
    weights.sort()
    maxN = 0

    for weight in weights:
        if weight > maxN + 1:
            return maxN + 1
        else:
            maxN = maxN + weight

    return maxN+1


def main():
    n = int(input())
    weights = list(map(int,input().split()))
    print(solution(n,weights))

main()