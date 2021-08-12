import sys
n,l = map(int,input().split())

mat = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

n_possible_way = 0

# 가로 직접 다 해보기 # row check
for i in range(n):
    prev = mat[i][0]
    cnt_l_prev = 0
    cnt_l = 0
    is_l_check = 0

    for j in range(1,n):
        if prev == mat[i][j]+1 and not is_l_check:
            cnt_l_prev = 0
            is_l_check = 1
            cnt_l = 1
        elif prev == mat[i][j] - 1:
            if cnt_l_prev < l:
                break
            cnt_l_prev = 0
        elif prev == mat[i][j]:
            cnt_l_prev = cnt_l_prev + 1
            if is_l_check:
                cnt_l = cnt_l + 1
                if cnt_l >= l:
                    is_l_check = 0
        elif abs(prev - mat[i][j]) > 1 and is_l_check:
            break
        prev = mat[i][j]
    else:
        n_possible_way = n_possible_way + 1

# col check
for j in range(n):
    prev = mat[i][0]
    cnt_l_prev = 0
    cnt_l = 0
    is_l_check = 0

    for i in range(1,n):
        if prev == mat[i][j]+1 and not is_l_check:
            cnt_l_prev = 0
            is_l_check = 1
            cnt_l = 1
        elif prev == mat[i][j] - 1:
            if cnt_l_prev < l:
                break
            cnt_l_prev = 0
        elif prev == mat[i][j]:
            cnt_l_prev = cnt_l_prev + 1
            if is_l_check:
                cnt_l = cnt_l + 1
                if cnt_l >= l:
                    is_l_check = 0
        elif abs(prev - mat[i][j]) > 1 and is_l_check:
            break
        prev = mat[i][j]
    else:
        n_possible_way = n_possible_way + 1



print(n_possible_way)