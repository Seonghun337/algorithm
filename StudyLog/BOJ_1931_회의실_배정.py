# return minimun index of value with sorted array
def lowerBound(array, a, b, value):
    mid = (a+b)//2
    if len(array) == 0:
        return 0

    if mid == a:
        if array[a] > value:
            return a
        else:
            return a + 1
        # return mid + 1

    if array[mid] > value:
        return lowerBound(array, a, mid, value)
    else:
        return lowerBound(array, mid, b, value)



n = int(input())
meets = []
for _ in range(n):
    meets.append(tuple(map(int,input().split())))

meets.sort()

dp = []

# start는 검사할 때
# end는 저장할 때
# dp[i]는 i개 회의 할 때 최소 끝나는 시점
for meet in meets:
    start, end = meet
    idx = lowerBound(dp,0,len(dp),start)
    if idx==len(dp):
        dp.append(end)
    else:
        if end < dp[idx]:
            dp[idx] = end

# print(dp)
print(len(dp))

# print(lowerBound([6],0,1,1))