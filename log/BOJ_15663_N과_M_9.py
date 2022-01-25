n,m = map(int,input().split())

import sys

nums = list(map(int,sys.stdin.readline().rstrip().split()))


nums.sort()

def search(nums,m,arr=[],k=0):
    if k == m:
        print(*arr)
    else:
        prev = 0
        for i in range(len(nums)):
            if nums[i] != prev:
                tmp = nums[i]
                arr.append(tmp)
                del nums[i]
                search(nums,m,arr,k+1)
                del arr[-1]
                nums.insert(i,tmp)
                prev = tmp


search(nums,m)