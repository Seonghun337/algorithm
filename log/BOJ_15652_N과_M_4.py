n,m = map(int,input().split())

nums = []
def search(nums,k,n,d,m):
    if d==m:
        print(' '.join(map(str,nums)))
    else:
        for i in range(k,n+1):
            nums.append(i)
            search(nums,i,n,d+1,m)
            del nums[-1]

search(nums,1,n,0,m)