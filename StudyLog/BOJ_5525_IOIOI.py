# # n = int(input())
# # m = int(input())

# # import sys

# # line = list(sys.stdin.readline().rstrip())

# # cnt = 0

# # for i in range(0, m-2*n-1):
# #     if line[i] == 'O':
# #         continue

# #     isI = 0
# #     for j in range(1,n*2+1):
# #         if isI == 0 and line[i+j]!='O':
# #             break
# #         elif isI == 1 and line[i+j]!='I':
# #             break

# #         if isI == 0:
# #             isI = 1
# #         else:
# #             isI = 0
# #     else:
# #         cnt = cnt + 1

# # print(cnt)


# n = int(input())
# m = int(input())

# import sys
# line = list(sys.stdin.readline().rstrip())

# cons = []

# prev = line[0]
# con_tmp = 1


# Istart = 1 if prev == 'I' else 0

# for i in range(1,m):
#     if line[i] != prev:
#         con_tmp = con_tmp + 1
#     else:
#         cons.append((con_tmp, Istart))
#         con_tmp = 1
#         Istart = 1 if line[i] == 'I' else 0

#     prev = line[i]

# cons.append((con_tmp, Istart))

# # print(cons)

# ans = 0

# # c = 부분 순열 길이
# # b = 시작하는 원소
# # ex) 4,1 -> IOIO
# # 홀수일때랑 짝수일때랑 다름

# # 홀/짝 * I/O -> O개수
# # 홀I = (c-1)/2
# # 홀O = (c-3)/2
# # 짝I/O = (c-2)/2

# # 위 부분 순열 안에 Pn이 c-n+1 개 들어감
# # c > n 일 때만 계산
# for con in cons:
#     c, b = con
#     if c > n:
#         # ans = ans + c - n
#         if c % 2 == 0:
#             ans = ans + (c-2)//2 - n + 1
#         else:
#             if b==1:
#                 ans = ans + (c-1)//2 - n + 1
#             else:
#                 ans = ans + (c+3)//2 - n + 1

# print(ans)
        

n = int(input())
m = int(input())

import sys
line = list(sys.stdin.readline().rstrip())

ans = 0
cnt_tmp = 0
prev = ''
cnt_on = 0

for x in line:
    if cnt_on == 0:
        if x=='I':
            cnt_on = 1
            prev = x
            continue
        else:
            prev = x
            continue
    
    if prev == 'O' and x == 'I':
        cnt_tmp = cnt_tmp + 1
        if cnt_tmp >= n:
            ans = ans + 1

    elif x == prev:
        cnt_tmp = 0
        if x == 'O':
            cnt_on = 0

    prev = x
    


print(ans)