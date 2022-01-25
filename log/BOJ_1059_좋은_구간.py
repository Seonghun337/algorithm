#2021-04-06
import sys

def solution(L,S,n):
    S.sort()

    a,b = 0,0
    for i in range(len(S)):
        if S[i] > n:
            if i==0:
                a,b = 0,S[i]
            else:
                a,b = S[i-1],S[i]
            break

    # print(a+1,b-1)
    return count(a+1,b-1,n)

def count(a,b,n):#[a,b]에 속하는 부분 구간 중 n을 포함한 부분 구간의 개수를 count
    cnt = 0
    for i in range(a,b+1):
        for j in range(i+1,b+1):
            if i <= n and n <= j:
                # print(i,j)
                cnt = cnt+1
    return cnt

def main():
    L = int(input())
    S = list(map(int,sys.stdin.readline().rstrip().split()))
    n = int(input())

    print(solution(L,S,n))

main()