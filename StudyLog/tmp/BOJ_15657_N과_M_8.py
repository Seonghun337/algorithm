n,m = map(int,input().split())
nums = list(map(int,input().split()))

nums.sort()

def comb(lst,n,m,k):
    if len(lst) == m:
        print(*lst)
        return

    for i in range(k,n):
        lst.append(nums[i])
        comb(lst,n,m,i)
        lst.remove(nums[i])


comb([],n,m,0)