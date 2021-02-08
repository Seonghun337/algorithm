
def solution(n,arr):
    result = []

    for n in arr:
        if len(result) == 0:
            result.append(n)
        if result[-1] < n:
            result.append(n)
        else:
            lower_bound(result, n, 0, len(result)-1)

    return len(result)

def lower_bound(arr,n,start,end):
    mid = (start+end)//2
    if start > end:
        return

    if mid==0:
        if arr[0] > n:
            arr[0] = n
            return

    if arr[mid] > n and arr[mid-1] < n:
        arr[mid] = n
    else:
        if arr[mid] >= n:
            lower_bound(arr,n,start,mid-1)
        else:
            lower_bound(arr,n,mid+1,end)


def main():
    n = int(input())
    arr = list(map(int,input().split()))
    print(solution(n,arr))
    # a = [3,4,5,6]
    # lower_bound(a,2,0,3)
    # print(a)

main()