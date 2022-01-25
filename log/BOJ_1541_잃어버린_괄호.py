# 어려워 보이지만 규칙은 단순함
# 식을 최소로 만들기 위해서 - 뒤에 오는 + 는 모두 -방향으로 바꿀 수 있음

def getSum(s):
    return sum(list(map(int,s.split('+'))))

import sys
eq = sys.stdin.readline().rstrip().split('-')

result = getSum(eq[0])

for i in range(1,len(eq)):
    result = result - getSum(eq[i])

print(result)