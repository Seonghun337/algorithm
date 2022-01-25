import sys
n = int(input())
nums = list(map(int,sys.stdin.readline().rstrip().split()))

nums.sort()
print(nums[(n-1)//2])