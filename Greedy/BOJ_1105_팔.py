def solution(L,R):
    strL, strR = map(str,(L,R))
    #길이 맞추기
    if len(strL) > len(strR):
        strR = ('0'*(len(strL) - len(strR))) + strR
    else:
        strL = ('0'*(len(strR) - len(strL))) + strL

    # print(strL)
    # print(strR)
    #왼쪽부터 연속으로 둘 다 8인지 검사
    cnt = 0
    for i in range(len(strL)):
        # print(strL[i])
        # print(strR[i])

        if strL[i] != strR[i]:
            break
        elif strL[i] == strR[i] and strL[i] == '8':
            cnt = cnt + 1

    
    return cnt

def main():
    L,R = map(int,input().split())
    print(solution(L,R))


main()