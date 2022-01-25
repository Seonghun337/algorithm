n,m = map(int,input().split())
nums = list(set(map(int,input().split())))
n = len(nums)
nums.sort()

def search(d=0,arr=[]):
    if d==m:
        print(*arr)
    else:
        for i in range(n):
            arr.append(nums[i])
            search(d+1,arr)
            arr.pop()
search()