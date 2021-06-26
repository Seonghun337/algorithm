#코드 못찾아서 다시 품

n = int(input())
arr = list(map(int,input().split()))

dp = []

def lowerbound(arr,target):
    s = 0
    e = len(arr)

    while s < e:
        mid = (s+e)//2
        if arr[mid] < target:
            s = mid + 1
        else:
            e = mid
    return e



for a in arr:
    ni = lowerbound(dp,a)
    if ni == len(dp):
        dp.append(a)
    else:
        dp[ni] = min(a,dp[ni])

# print(dp)
print(len(dp))
