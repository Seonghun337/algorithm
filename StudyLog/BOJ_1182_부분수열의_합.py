n,s = map(int,input().split())
arr = list(map(int,input().split()))
# print(arr)
hist = []

for num in arr:
    tmp = []
    for h in hist:
        tmp.append(h + num)
    hist = hist + tmp
    hist.append(num)
    # print(hist)

print(hist.count(s))