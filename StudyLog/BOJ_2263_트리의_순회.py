import sys

n = int(input())
in_order = list(map(int,input().split())) # 왼 중 오
post_order = list(map(int,input().split())) # 왼 오 중

pre_order = [] # 중 왼 오


# 2 7 5 6 11  2  5 4 9
# 2 5 11 6 7   4 9 5   2


sys.setrecursionlimit = int(1000000)
def search(sub_in_order=in_order, sub_post_order=post_order):
    if len(sub_in_order) == len(sub_post_order) == 0:
        return

    if len(sub_in_order) == 1:
        pre_order.append(sub_in_order[0])
        return
    

    root = sub_post_order[-1]
    root_idx = sub_in_order.index(root)
    
    pre_order.append(root)

    search(sub_in_order[:root_idx], sub_post_order[:root_idx])
    search(sub_in_order[root_idx+1:], sub_post_order[root_idx:-1])


def search_v2(a_in=0, b_in=n, a_post=0, b_post=n):
    if b_in - a_in == 0:
        return

    if b_in - a_in == 1:
        pre_order.append(in_order[a_in])
        return


    root = post_order[a_post:b_post][-1]
    root_idx = in_order[a_in:b_in].index(root)
    
    pre_order.append(root)

    search_v2(a_in, a_in+root_idx, a_post, a_post+root_idx)
    search_v2(a_in + root_idx + 1, b_in, a_post + root_idx, b_post - 1)

def search_v3():
    stack = [(0,n,0,n)]
    
    while stack:
        a_in,b_in,a_post,b_post = stack.pop()

        if b_in - a_in <= 0:
            continue
        if b_in - a_in == 1:
            pre_order.append(in_order[a_in])
            continue

        root = post_order[a_post:b_post][-1]
        root_idx = in_order[a_in:b_in].index(root)
    
        pre_order.append(root)

        stack.append((a_in + root_idx + 1, b_in, a_post + root_idx, b_post - 1))
        stack.append((a_in, a_in+root_idx, a_post, a_post+root_idx))
        


# search_v3()
# print(*pre_order)



