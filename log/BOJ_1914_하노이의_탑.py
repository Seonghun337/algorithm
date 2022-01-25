def solution(n):
    # result = []
    print((2**n)-1)
    if n <= 20:
        func(n,1,2,3)
    # cnt = func(n,1,2,3,result)
    # print(cnt)
    # for line in result:
        # print(' '.join(map(str,line)))

def func(n,fromNum,midNum,toNum):
    if n==1:
        # result.append((fromNum,toNum))
        print(fromNum,toNum)
        return 1
    else:
        cnt = 0
        cnt = cnt + func(n-1,fromNum,toNum,midNum)
        cnt = cnt + func(1,fromNum,midNum,toNum)
        # result.append((fromNum,toNum))
        cnt = cnt + func(n-1,midNum,fromNum,toNum)
        return cnt

def main():
    n = int(input())
    solution(n)

main()