nums = [-1 for _ in range(1000001)]
#-1: 미탐색, 0: 합성수, 1: 소수
nums[1] = 0 #일단 소수가 아니므로
for i in range(2,1000001):
    if nums[i] == 0:
        continue
    else:
        nums[i] = 1
        k = 2
        while i*k < len(nums):
            nums[i*k] = 0
            k = k+1

m,n = map(int,input().split())
cnt = 0
for i in range(m,n+1):
    if nums[i] == 1:
        print(i)