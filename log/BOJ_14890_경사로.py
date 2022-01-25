import sys
n,l = map(int,input().split())

mat = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

n_possible_way = 0

# 행 검사
for i in range(n):
    prev = mat[i][0]
    n_cont = 0 # 연속된 칸 수(같은 높이가)
    checking = 0 # 내리막을 만나서 L을 카운트 하는중임을 나타내는 플래그 변수
    for j in range(1,n):
        # print(j)
        if prev == mat[i][j]:
            n_cont = n_cont + 1
            if checking == 1 and n_cont >= l:
                checking = 0
        elif prev == mat[i][j] + 1: #내리막
            # 이미 체크중인데 내리막을 또 만나면 불가능 판단
            if checking == 1:
                break
            else:
                n_cont = 1
                checking = 1
        elif prev == mat[i][j] - 1 and checking == 0: #오르막
            # 오르막 전에 L비트 있었으면 괜찮
            # L비트보다 작으면 오르막 불가능 판단
            if n_cont >= l:
                n_cont = 1
            else:
                break
        else:
            break
        prev = mat[i][j]
    else:
        n_possible_way = n_possible_way + 1
        print('i',i)



# 열 검사
for j in range(n):
    prev = mat[0][j]
    n_cont = 0 # 연속된 칸 수(같은 높이가)
    checking = 0 # 내리막을 만나서 L을 카운트 하는중임을 나타내는 플래그 변수
    for i in range(1,n):
        # print(i)
        if prev == mat[i][j]:
            n_cont = n_cont + 1
            if checking == 1 and n_cont >= l:
                checking = 0
        elif prev == mat[i][j] + 1: #내리막
            # 이미 체크중인데 내리막을 또 만나면 불가능 판단
            if checking == 1:
                break
            else:
                n_cont = 1
                checking = 1
        elif prev == mat[i][j] - 1 and checking == 0: #오르막
            # 오르막 전에 L비트 있었으면 괜찮
            # L비트보다 작으면 오르막 불가능 판단
            if n_cont >= l:
                n_cont = 1
            else:
                break
        else:
            break
        prev = mat[i][j]
    else:
        n_possible_way = n_possible_way + 1
        print('j',j)

print(n_possible_way)