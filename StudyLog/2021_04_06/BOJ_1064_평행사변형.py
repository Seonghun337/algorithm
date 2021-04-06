#2021-04-06
import math
import sys


def solution(x1,y1,x2,y2,x3,y3):
    # 세 점이 직선 상에 있는지 확인
    # 나누기 없이 직선의 방정식을 풀면 다음 식이 됨
    if (x2-x1)*(y3-y1) == (y2-y1)*(x3-x1):
        return -1.0

    d1 = getDistance(x1,y1,x2,y2)
    d2 = getDistance(x2,y2,x3,y3)
    d3 = getDistance(x3,y3,x1,y1)

    return (max(d1,d2,d3) - min(d1,d2,d3))*2
    
    # 거리 두개 합 최대-최소
def getDistance(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def main():
    x1,y1,x2,y2,x3,y3 = map(int,input().split())
    print(solution(x1,y1,x2,y2,x3,y3))

main()


