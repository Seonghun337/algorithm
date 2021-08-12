def solution(N,L):
    i = L

    while i <= 100:
        Sum = (i-1)*i//2
        if (N-Sum)%i == 0:
            k = (N-Sum)//i
            if k < 0:
                break
            answer = [x for x in range(k,k+i)]
            print(' '.join(map(str,answer)))
            return
        else:
            # Sum = Sum + i
            i = i + 1
            # print(Sum,i)

    print('-1')
    return

def main():
    N,L = map(int,input().split())
    solution(N,L)


main()