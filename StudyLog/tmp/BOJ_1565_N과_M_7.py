n,m = map(int,input().split())
nums = list(map(int,input().split()))

nums.sort()

def comb(lst,n,m,k):
    if len(lst) == m:
        print(*lst)
        return

    for i in range(n):
        lst.append(nums[i])
        comb(lst,n,m,i)
        lst.pop()


comb([],n,m,0)