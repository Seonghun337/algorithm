import sys,copy
import heapq

T = int(input())
inputs = []
for _ in range(T):
    n = int(input())
    nums = list(map(int,sys.stdin.readline().rstrip().split()))
    inputs.append(nums)

### 이 위는 입력과 관련된 부분

# 그리디 시도 -> dp 시도 -> 모르겠어서 찾아봄

# 배열을 분할하는 모든 경우의 수를 살펴 본다.
# 단, 특정 구간을 분할해서 합쳤을 때의 최솟값은
# 구간의 경계값에 의해 결정되므로... (외부와 독립)
# 구간의 최솟값을 한 번만 계산한 뒤 메모이제이션 할 수 있다.

def search(nums,dp={},a=0,b=len(nums)-1): # (a,b) 구간을 탐색한다. a 포함, b 포함
    # 구간의 최솟값 (다 합쳤을 때 최소 비용)을 탐색한다.
    # 계산한 후에는 dp에 저장한다.
    # dp는 (a,b) 구간을 의미하는 튜플을 키로, 그 구간의 최소 비용을 값으로 가지는 딕셔너리로 설정하였다.


    # 계산한 적이 있다면..
    if (a,b) in dp:
        return dp[(a,b)]

    # 구간의 길이가 2이면 두 개를 더하는 경우밖에 없다
    if b-a == 1:
        dp[(a,b)] = nums[a] + nums[b]
        return nums[a] + nums[b]
    
    # 구간의 길이가 1이면 본인을 반환한다
    if b-a == 0:
        dp[(a,b)] = nums[a]
        return nums[a]


    min_ = int(1e9)
    for i in range(1, b-1):
        min_ = min(min_, search(nums,dp,a,i) + search(nums,dp,i+1,b) + sum(nums[a:b+1]))

    dp[(a,b)] = min_
    return min_

# 위 search함수가 recursion error(setrecursionlimit(10**9) 까지 해도 error)
# 그래서 for문으로 다시 설계
def solution(nums):
    # 여기서는 
    n = len(nums)
    cost = {}
    sum_dp = [0, nums[0]]
    
    for i in range(n):
        cost[(i,i)] = nums[i] # 구간 1짜리는 다 본인
    
    for i in range(1,n):
        cost[(i-1,i)] = sum(nums[i-1:i+1])
        sum_dp.append(sum_dp[-1] + nums[i])

    # print(sum_dp)

    for l in range(2,n): # 구간의 길이

        for s in range(0,n-l): # 구간의 시작점

            cost[(s,s+l)] = int(1e9)
            for k in range(s,s+l): # 구간의 칸막이
                  
                # print(s,k,k+1,s+l)
                # cost[(s,s+l)] = min(cost[(s,s+l)], cost[(s,k)] + cost[(k+1,s+l)] + sum(nums[s:s+l+1])  - (nums[s] if k==s else 0) - (nums[s+l] if k == s+l-1 else 0))#+ sum(nums[s:s+l+1]))
                sum_ = 0
                if k == s:
                    sum_ = sum_dp[s+l+1] - sum_dp[s+1]
                elif k == s+l-1:
                    sum_ = sum_dp[s+l] - sum_dp[s]
                else:
                    sum_ = sum_dp[s+l+1] - sum_dp[s]
                # print('s',l,s,k,sum_)
                     #- (nums[s] if k==s else 0) - (nums[s+l] if k == s+l-1 else 0) # 이번 합치기의 비용 추가
                cost[(s,s+l)] = min(cost[(s,s+l)], cost[(s,k)] + cost[(k+1,s+l)] + sum_)#+ sum(nums[s:s+l+1]))
            # print(cost)
                
    
    # print(cost)
    return cost[(0,n-1)]

# 테스트케이스마다 search함수를 실행
for inp in inputs:
    # print(inp)
    # print(search(nums))
    print(solution(inp))



