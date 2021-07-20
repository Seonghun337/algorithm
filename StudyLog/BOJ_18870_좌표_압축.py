n = int(input())

import sys,copy
_nums = list(map(int,sys.stdin.readline().rstrip().split()))
result = []
trans = {}
now = 0

nums = copy.deepcopy(_nums)
nums.sort()

for num in nums:
    if num in trans:
        result.append(trans[num])
    else:
        trans[num] = now
        result.append(now)
        now = now + 1
        
for num in _nums:
    print(trans[num],end=' ')

