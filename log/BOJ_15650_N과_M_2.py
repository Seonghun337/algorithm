n,m = map(int,input().split())

def func_(nums,k,m,set_):
    if len(set_) == m:
        print(' '.join(list(map(str,set_))))
    else:
        if k >= len(nums):
            return
        else:
            for i in range(k,len(nums)):
                set_.append(nums[i])
                func_(nums,i+1,m,set_)
                set_.remove(nums[i])
                func_(nums,i+1,n,set_)


nums = [x for x in range(1,n+1)]
set_ = []
func_(nums,0,m,set_)




