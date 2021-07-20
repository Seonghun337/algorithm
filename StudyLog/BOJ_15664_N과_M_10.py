n,m = map(int,input().split())

nums = list(map(int,input().split()))

nums.sort()

def search(d=0,arr=[],i=0):
    if d==m:
        print(*arr)
    else:
        prev = -1
        for j in range(i,n):
            if nums[j] != prev:
                arr.append(nums[j])
                search(d+1,arr,j+1)
                arr.pop()
            prev = nums[j]


search()