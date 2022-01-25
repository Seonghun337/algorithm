import math

def getStrNinK(n,k):
    res = ''
    d = int(math.log(n,k))
    # print(d)
    while n > 0:
        res += str(n//(k**d))
        n %= (k**d)
        d -= 1
        
    return res

def isPrime(n):
    if n == 1:
        return False
    
    for num in range(2,int(n**(1/2))+1):
        if n % num == 0:
            return False
    else:
        return True

def solution(n, k):
    # 나올 수 있는 가장 높은 소수는 1,000,000을 3진수로 바꿨을 때 모든 자릿수가 하나의 소수인 경우
    # 최대 12자리..?
    
    # 소수를 미리 구해놓습니다
#     MAX_P = int(1e7) #일단 여기까지만
#     primes = set()
    
#     nums = [0 for _ in range(MAX_P)]
#     for n in range(2,MAX_P):
#         if nums[n] == 0:
#             primes.add(n)
#             k = 2
#             while n*k < MAX_P:
#                 nums[n*k] = 1
#                 k += 1
    
    # n을 k진수로 변환합니다. 문자열 타입으로 리턴합니다.
    strN = getStrNinK(n,k)
    
    print(strN)
    answer = 0
    strN = strN.split('0')
    
    print(strN)
    for subS in strN:
        if subS != '':
            if isPrime(int(subS)):
                answer += 1
            # if int(subS) in primes:
                # answer += 1
    
    # answer = -1
    return answer