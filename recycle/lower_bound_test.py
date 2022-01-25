import random

n = 20

nums = []
for _ in range(n):
    nums.append(random.randrange(1,100))

nums.sort()

print(*nums)

target = 19


a = 0
b = len(nums)

while a < b:
    mid = (a+b)//2

    if nums[mid] >= target:
        b = mid
    else:
        a = mid + 1

print(b,nums[b])


