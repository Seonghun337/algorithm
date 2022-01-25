n,m = map(int,input().split())
nums = list(set(map(int,input().split())))
n = len(nums)

nums.sort()

def search(d=0,i=0,arr=[]):
    if d==m:
        print(*arr)
    else:
        for j in range(i,n):
            arr.append(nums[j])
            search(d+1,j,arr)
            arr.pop()

search()