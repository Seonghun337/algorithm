def factorial(n):
    if n <= 1:
        return 1
    else:
        return factorial(n-1)*n

def solve(n,m):
    #mCn
    return int(factorial(n) / (factorial(m) * factorial(n-m)))
    
n = int(input())


answerList = []
for i in range(n):
    (n,m) = input().split(' ')
    answerList.append(solve(int(m),int(n)))

for answer in answerList:
    print(answer)



