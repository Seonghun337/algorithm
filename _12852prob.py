def solution(n):
    
    arr = [0] * 1000001
    prev = [0] * 1000001


    for i in range(2, n+1):
        arr[i] = arr[i-1]+1
        prev[i] = i-1
        if i%3 == 0:
            newR = arr[i//3]+1
            if arr[i] > newR:
                arr[i] = newR
                prev[i] = i//3
        if i%2 == 0:
            newR = arr[i//2]+1
            if arr[i] > newR:
                arr[i] = newR
                prev[i] = i//2

    result = []
    idx = n
    while idx != 1:
        result.append(str(idx))
        idx = prev[idx]
        
    result.append('1')

    return arr[n],result

def main():
    n = int(input())
    mi,result = solution(n)
    print(mi)
    print(' '.join(result))

main()