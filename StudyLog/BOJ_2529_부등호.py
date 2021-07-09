k = int(input())
import sys
ineqs = list(sys.stdin.readline().rstrip().split())

    
def getValidIneqs(ineqs, reverse = False):
    if reverse: # >
        n = len(ineqs)+1
        result = [0 for _ in range(n)]
        for i in range(n-2,-1,-1):
            if ineqs[i] == '>':
                for j in range(i,-1,-1):
                    result[j] = result[j] + 1
                    if j > 0 and ineqs[j-1] != '>': 
                        break
        return result
    else: # <
        # n = len(ineqs)+1
        # result = [0 for _ in range(n)]
        # for i in range(len(ineqs)):
        #     if ineqs[i] == '<':
        #         for j in range(i+1,n):
        #             result[j] = result[j] + 1
        #             if j < n-1 and ineqs[j] != '<': 
        #                 break
        # return result
        n = len(ineqs)+1
        result = [0 for _ in range(n)]
        for i in range(n-2,-1,-1):
            if ineqs[i] == '<':
                for j in range(i,-1,-1):
                    result[j] = result[j] + 1
                    if j > 0 and ineqs[j-1] != '<': 
                        break
        return result

def searchMax(ineqs,k):
    v_ineqs = getValidIneqs(ineqs)
    nums = [x for x in range(9,8-k,-1)]
    result = []
    for i in range(k+1):
        result.append(nums[v_ineqs[i]])
        del nums[v_ineqs[i]]
    return ''.join(list(map(str,result)))

def searchMin(ineqs,k):
    v_ineqs = getValidIneqs(ineqs, reverse=True)
    nums = [x for x in range(0,k+1)]
    result = []
    for i in range(k+1):
        result.append(nums[v_ineqs[i]])
        del nums[v_ineqs[i]]
    return ''.join(list(map(str,result)))

print(searchMax(ineqs,k))
print(searchMin(ineqs,k))

