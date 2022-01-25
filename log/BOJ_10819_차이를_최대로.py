n = int(input())

nums = list(map(int,input().split()))

max_val = -1

def getValue(arr):
    result = 0

    prev = arr[0]
    for val in arr[1:]:
        result = result + abs(prev-val)
        prev = val

    return result


from itertools import permutations

permus = permutations(nums)
for p in permus:
    v = getValue(p)
    if max_val < v:
        max_val = v

print(max_val)