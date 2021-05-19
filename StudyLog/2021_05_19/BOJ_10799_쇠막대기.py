import sys

line = list(sys.stdin.readline().rstrip())

sum_ = 0
# now = 0
prev = ''
stack = []
for s in line:
    if s == '(':
        stack.append(s)
    elif s==')':
        if prev == '(':
            stack.pop()
            sum_ = sum_ + len(stack)
        else:
            stack.pop()
            sum_ = sum_ + 1
    prev = s

print(sum_)
