import sys

global Maximum

def solution(n, arr):
    global Maximum
    answer = [[-1 for _ in range(n)] for __ in range(n)]

    Maximum = 1

    # stack = []

    for i in range(n):
        for j in range(n):
            stack = []
            stack.append((i,j))


            while len(stack) > 0:
                y,x = stack[-1]
                
                
                if answer[y][x] != -1:
                    stack.pop()
                    # print('---',stack.pop())
                    continue

                M = 1
                if y > 0 and arr[y][x] < arr[y-1][x]:
                    if answer[y-1][x] == -1:
                        stack.append((y-1,x))
                        continue
                    else:
                        M = max(answer[y-1][x]+1, M)
                
                if y < n-1 and arr[y][x] < arr[y+1][x]:
                    if answer[y+1][x] == -1:
                        stack.append((y+1,x))
                        continue
                    else:
                        M = max(answer[y+1][x]+1, M)

                if x > 0 and arr[y][x] < arr[y][x-1]:
                    if answer[y][x-1] == -1:
                        stack.append((y,x-1))
                        continue
                    else:
                        M = max(answer[y][x-1]+1, M)

                if x < n-1 and arr[y][x] < arr[y][x+1]:
                    if answer[y][x+1] == -1:
                        stack.append((y,x+1))
                        continue
                    else:
                        M = max(answer[y][x+1]+1, M)

                answer[y][x] = M
                if Maximum < M:
                    Maximum = M
                stack.pop()
                # print(stack.pop())
                
    # print(answer)
                


    # print(answer)
    return Maximum


def search(n, arr, y, x, answer):
    global Maximum

    if answer[y][x] != -1:
        return answer[y][x]

    M = 1
    if y > 0 and arr[y][x] < arr[y-1][x]:
        M = max(M,search(n, arr, y-1, x, answer)+1)
    
    if y < n-1 and arr[y][x] < arr[y+1][x]:
        M = max(M,search(n, arr, y+1, x, answer)+1)

    if x > 0 and arr[y][x] < arr[y][x-1]:
        M = max(M,search(n, arr, y, x-1, answer)+1)

    if x < n-1 and arr[y][x] < arr[y][x+1]:
        M = max(M,search(n, arr, y, x+1, answer)+1)

    answer[y][x] = M
    if M > Maximum:
        Maximum = M
    return M

def main():
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int,sys.stdin.readline().rstrip().split())))
    print(solution(n, arr))

main()




#                 #if 갈 곳 없음
#                 answer[y][x] = 1
#                 stack.pop()

#                 #if 갈 곳 있음 + 갈 곳들 이미 모두 방문함
#                 #+1 한 값중 최댓값 넣고 pop

#                 #if 갈 곳 있음 + 방문 안함
#                 #푸시 후 계속