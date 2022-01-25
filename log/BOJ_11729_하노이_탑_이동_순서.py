n = int(input())

answer = [0]

def move(a,b,n,c):
    #a 에서 b로 옮기는 데 a에 n개가 쌓여있음
    if n==1:
        answer[0] = answer[0] + 1
        answer.append((a,b))
    else:
        # move(a,c,1,b)
        # move(a,b,n-1,c)
        # move(c,b,1,a)
        move(a,c,n-1,b)
        move(a,b,1,c)
        move(c,b,n-1,a)

move(1,3,n,2)

print(answer[0])
for output in answer[1:]:
    print(*output)