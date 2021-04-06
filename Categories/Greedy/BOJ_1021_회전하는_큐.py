#21.02.01
# * 큐를 회전하는 대신 포인터 인덱스를 선언하여 큐의 첫번째 원소를 가리키게 하면 상수시간에 회전


def solve(n, inputRow):
    cnt = 0
    ptrIdx = 0
    queue = [i+1 for i in range(n)]

    for i in inputRow:
        targetIdx = queue.index(i)
        l = len(queue)
  
        d = abs(targetIdx - ptrIdx)
        if d < l - d:
            cnt = cnt + d
        else:
            cnt = cnt + (l - d)

        ptrIdx = targetIdx
        queue.remove(i)
        if targetIdx == len(queue):
            targetIdx = targetIdx - 1


    return cnt



def main():
    N = list(map(int,input().split(' ')))[0]
    inputRow = list(map(int,input().split(' ')))
    print(solve(N, inputRow))

main()