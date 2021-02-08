def solution(n,m,nlist,mlist):
    result = []

    nlist.sort()
    for target in mlist:
        result.append(binsearch(nlist,target,0,n-1))

    return result

def binsearch(lst,target,start,end):
    mid = (start+end)//2
    if lst[mid] == target:
        return 1
    if end-start < 1:
        return 0
    
    if target <= lst[mid]:
        return binsearch(lst,target,start,mid-1)
    else:
        return binsearch(lst,target,mid+1,end)

def main():
    n = int(input())
    nlist = list(map(int,input().split()))
    m = int(input())
    mlist = list(map(int,input().split()))
    
    answer = solution(n,m,nlist,mlist)
    for a in answer:
        print(a)

main()