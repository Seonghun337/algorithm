# 7P5 / (3!2!) = 210?
# N <= 11 이니까 연산자가 들어갈 수 있는 자리는 최대 10
# 주어질 수 있는 연산자의 개수는 최대 40
# 40P10 -> 줜나 큰 숫자
# 중복 고려해서 10!*4 로 나누면 대략 2e11 -> 브루트포스는 안될듯
# 사용할 수 있는 연산자의 개수가 한정되어 있어서 dp도 안됨
# 
# 연산자 우선순위를 무시한다? 음....
# 브루트포스로 하되, 이전 연산 결과를 다시 계산하지 않으면 시간안에 될수도? 2초니까

# 나누기에 장난질 해놨네

n = int(input())
nums = list(map(int,input().split()))
ops = list(map(int,input().split()))

INF = int(1e9)

maxValue = -INF
minValue = INF

def search(ops, prev=nums[0] , d=1):
    global maxValue
    global minValue

    if d == n:
        if maxValue < prev :
            maxValue = prev
        if minValue > prev:
            minValue = prev
    else:
        for op in range(4):
            if ops[op] > 0:
                ops[op] = ops[op] - 1
                if op == 0:
                    search(ops, prev+nums[d], d+1)
                elif op == 1:
                    search(ops, prev-nums[d], d+1)
                elif op == 2:
                    search(ops, prev*nums[d], d+1)
                elif op == 3:
                    if prev < 0:
                        search(ops, -(abs(prev)//nums[d]), d+1)
                    else:
                        search(ops, prev//nums[d], d+1)
                ops[op] = ops[op] + 1

search(ops)

print(maxValue)
print(minValue)