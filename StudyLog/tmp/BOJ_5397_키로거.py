# n = int(input())

# def solution(keylog):
#     cursor = 0
#     buffer = []
#     for key in keylog:
#         if key == '<':
#             cursor = max(0,cursor-1)
#             continue
#         if key == '>':
#             cursor = min(len(buffer),cursor+1)
#             continue
#         if key == '-':
#             if cursor > 0:
#                 del buffer[cursor-1]
#                 cursor = max(0,cursor - 1)
#             continue
        
#         buffer.insert(cursor,key)
#         cursor = min(len(buffer),cursor + 1)
#         print(key,cursor,buffer)
#     return buffer

# keylogs = []
# for _ in range(n):
#     keylogs.append(list(str(input())))
    
# for keylog in keylogs:
#     print(''.join(solution(keylog)))

n = int(input())
keylogs = []
for _ in range(n):
    keylogs.append(list(str(input())))
    


def solution(keylog):
    left = []
    right = []

    for key in keylog:
        if key == '<':
            if len(left) > 0:
                right.append(left.pop())
        elif key == '>':
            if len(right) > 0:
                left.append(right.pop())
        elif key == '-':
            if len(left) > 0:
                left.pop()
        else:
            left.append(key)
    right.reverse()
    return left+right
        
for keylog in keylogs:
    print(''.join(solution(keylog)))