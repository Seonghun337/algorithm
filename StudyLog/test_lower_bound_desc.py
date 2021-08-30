nums = [8,6,5,4,2]

new_nums = [9,6,2,4,5]

a = 0
b = len(nums)

while a < b:
    mid = (a+b) // 2
    if nums[mid] < 7:
        b = mid
    else:
        a = mid+1

print(a)
