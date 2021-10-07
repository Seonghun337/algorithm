import sys

n = int(input())
nums = sorted(list(map(int,sys.stdin.readline().rstrip().split())))


a = 0
b = n-1

min_a = nums[0]
min_b = nums[-1]
min_value = nums[0] + nums[-1]

while a < b:
    now = nums[a] + nums[b]
    if abs(now) <= abs(min_value):
        min_value = now
        min_a, min_b = a,b

    if now >= 0:
        b -= 1
    else:
        a += 1

print(nums[min_a], nums[min_b])