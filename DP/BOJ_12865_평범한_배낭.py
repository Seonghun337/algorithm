def solution(n,k,objs):
    arr = [[0 for _ in range(k+1)] for __ in range(n)]
    M = 0

    for i in range(n):
        for j in range(k+1):
            w,v = objs[i]
            #
            if k==0:
                arr[i][j] = 0
            #
            #if i==0:
            if j < w:
                if i==0:
                    arr[i][j] = 0
                else:
                    arr[i][j] = arr[i-1][j]
            else:
                if i==0:
                    arr[i][j] = v
                else:
                    arr[i][j] = max(arr[i-1][j],arr[i-1][j-w]+v)

            if arr[i][j] > M:
                M = arr[i][j]

    return M


def main():
    n,k = map(int,input().split())
    objs = []
    for _ in range(n):
        w,v = map(int,input().split())
        objs.append((w,v))
    
    print(solution(n,k,objs))

main()


#prob12865_첫번째풀이_실패 왜 안되는지 생각해보기