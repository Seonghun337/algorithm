import sys

def solution(n,info):
    answer = [-1 for _ in range(n)]
    for i in range(n):
        cnt = 0
        j = 0
        while cnt != info[i] or answer[j] != -1:
            if answer[j] == -1:
                cnt = cnt + 1
            j = j + 1
        answer[j] = i+1
        # print(answer)
    return answer

def main():
    n = int(input())
    info = list(map(int,sys.stdin.readline().rstrip().split()))
    answer = solution(n,info)
    print(' '.join(map(str,answer)))

main()