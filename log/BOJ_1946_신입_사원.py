# BOJ_2565_전깃줄과 유사함
# 이번엔 교점이 있어야함
# 서류 심사 점수순으로 일단 정렬해놓으면
# 나중에 검사한 원소가 서류 심사 점수는 무조건 높은 것이니 (동석차 없음)
# 면접 성적은 여태 나온 면접 성적보다 낮아야 함 (하나라도 더 큰게 있으면 걔는 뽑히지 못함)
# 따라서 가장 긴 감소하는 부분 수열 문제로 치환할 수 있음

# 입력이 100,000이라서 n^2은 안됨. nlogn으로 하려면 앞부분에서 찾을 때 이진 탐색해야함
# dp 배열은 항상 내림차순으로 되어있음. 만약 아니라면? dp를 업데이트 할 게 남았다는 거니까 모순


import bisect
# 가장 긴 감소하는 부분 수열 문제
def solution(n, nums):
    # dp = [0 for _ in range(n)] # 내림차순(비오름차순?) 정렬되어 있을 것임
    # dp = [0 for _ in range(n)]
    dp = [0]
    
    for num in nums:
        #dp에서 num보다 작은 값이 처음 나오는 인덱스에 num으로 업데이트
        a = 0
        b = len(dp)
        while a < b:
            mid = (a+b) // 2
            if dp[mid] < num:
                b = mid
            else:
                a = mid + 1
        
        # dp[a] = num
        
        if a == len(dp)-1:
            dp.insert(a,num)
        else:
            dp[a] = num
        # dp.insert(bisect.bisect_right(dp, num),num)

    # print(dp)
    return len(dp)-1



import sys, heapq
T = int(input())

ans = []

inputs = []

for _ in range(T):
    n = int(input())
    tups = []
    for __ in range(n):
        heapq.heappush(tups,tuple(map(int,sys.stdin.readline().rstrip().split())))
    nums = []
    for __ in range(n):
        nums.append(heapq.heappop(tups)[1])
    inputs.append((n,nums))
    

for i in inputs:
    n,nums = i
    print(solution(n,nums))

