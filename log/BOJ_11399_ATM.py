import sys

n = int(input())
arr = list(map(int,sys.stdin.readline().rstrip().split()))

arr.sort()
Sum = 0
k = n
for c in arr:
    Sum = Sum + c*k
    k = k - 1
print(Sum)