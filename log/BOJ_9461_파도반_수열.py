T = int(input())

arr = [0, 1, 1, 1]

for i in range(4,101):
    arr.append(arr[i-2] + arr[i-3])

inputs = []
for i in range(T):
    inputs.append(int(input()))

for i in inputs:
    print(arr[i])