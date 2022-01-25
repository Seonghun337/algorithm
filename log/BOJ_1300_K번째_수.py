# A
# 1 2 3 4
# 2 4 6 8
# 3 6 9 12
# 4 8 12 16

# B
# 1 2 2 3 3 4 4 4 6 6 8 8 9 12 12 16

# 그대로 하면 시간초과

# 배열 B는 오름차순 정렬되어 있음 -> 정답 범위 내에서 이진 탐색 가능

# 정렬전, 배열 A의 각 행도 정렬되어 있음 -> 한 경우에 대해서 이진 탐색 가능(k번째가 맞는지 확인)
# 각 행의 값이 규칙이 있는 수열이므로, 상수시간으로 계산 가능

def main():
    n = int(input())
    k = int(input())

    answer = 0

    MIN_VALUE = 1
    MAX_VALUE = n*n
    a = MIN_VALUE
    b = MAX_VALUE

    while a <= b:
        mid = (a+b) // 2

        if count(n, mid) >= k:
            answer = mid
            b = mid - 1
        else:
            a = mid + 1
    
    print(answer)


def count(n, target):
    sum = 0
    for i in range(n):
        sum += countRow(n,i+1,target)
    return sum

# target보다 작거나 같은 원소의 개수 = target을 초과한 값이 처음 나오는 인덱스 (n개를 넘을 수는 없음)
def countRow(n, row_idx, target):
    return min(target//row_idx, n)


main()