T = int(input())

arr = [0, 1, 1, 1]

for i in range(4,101):
    arr.append(arr[i-2] + arr[i-3])


for i in range(T):
    print(arr[int(input())])