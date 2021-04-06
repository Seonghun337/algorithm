def solution(n,k,objs):
    answer = [0 for _ in range(k+1)]
    selected = [0 for _ in range(n)]
    for i in range(k,-1,-1):
        result = func(i,selected,objs,answer)
    # print(answer)
    return result

def func(k,selected,objs,answer):
    if answer[k] != 0:
        return answer[k]

    # M = 0

    for i in range(len(objs)):
        w,v = objs[i]
        if selected[i] == 0 and k-w >= 0:
            selected[i] = 1            
            answer[k] = max(answer[k],func(k-w,selected,objs,answer)+v)
            selected[i] = 0

    return answer[k]


def main():
    n,k = map(int,input().split())
    objs = []
    for _ in range(n):
        w,v = map(int,input().split())
        objs.append((w,v))
    
    print(solution(n,k,objs))

main()
