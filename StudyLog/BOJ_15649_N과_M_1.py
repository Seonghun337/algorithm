n,m = map(int,input().split())

def func(nums,m,set_):
    if len(set_) == m:
        print(' '.join(list(map(str,set_))))
        return
    else:
        for el in nums:
            if el not in set_:
                set_.append(el)
                func(nums,m,set_)
                set_.remove(el)


nums = [x for x in range(1,n+1)]
set_ = []
func(nums,m,set_)




# def func_(nums,k,m,set_):
#     if len(set_) == m:
#         print(' '.join(list(map(str,set_))))
#     else:
#         if k >= len(nums):
#             return
#         else:
#             for i in range(k,len(nums)):
#                 set_.append(nums[i])
#                 func_(nums,i+1,m,set_)
#                 set_.remove(nums[i])
#                 func_(nums,i+1,n,set_)