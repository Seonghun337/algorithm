def solution(s,n,k,r1,r2,c1,c2):
    answer = [[0 for _ in range(c2-c1+1)] for __ in range(r2-r1+1)]
    for y in range(r1,r2+1):
        for x in range(c1,c2+1):
            answer[y-r1][x-c1] = isBlack(y,x,n,k,s)
    return answer

def isBlack(y,x,n,k,d):
    #if 가운데 -> 1 리턴
    #else d-1 recursion
    #d==1이면 바로 계산
    lowerBound = (n-k)/2    #(n,k)=(3,1) 일 때 1
    upperBound = n - (n-k)/2    # 2
    unitLength = n**(d-1)

    if x < upperBound*unitLength and \
        x >= lowerBound*unitLength and \
            y < upperBound*unitLength and \
                y >= lowerBound*unitLength:
        return 1
    else:
        if d <= 1:
            return 0
        else:
            return isBlack(y%unitLength,x%unitLength,n,k,d-1)

def main():
    s,n,k,r1,r2,c1,c2 = map(int,input().split())
    answer = solution(s,n,k,r1,r2,c1,c2)
    for line in answer:
        print(''.join(map(str,line)))

main()

#출력할때 공백 주의
#s가 0일수도 있음 그래서 리컬전 이스케이프를 d==1로 할 경우 무한 재귀
# 분할 정복인가?
