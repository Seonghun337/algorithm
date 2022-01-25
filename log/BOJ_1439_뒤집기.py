#2021-04-07
import sys

def solution(S):
    return min(countPiece(S,'0'),countPiece(S,'1'))

def countPiece(S,n):
    result = 0
    prev = -1
    for i in range(len(S)):
        # print(S[i],prev,result)
        if S[i] == n and prev != n:
            result = result + 1
            prev = n
        prev = S[i]
    return result

def main():
    print(solution(list(sys.stdin.readline().rstrip())))


main()