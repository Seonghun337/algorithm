import sys

line = list(sys.stdin.readline().rstrip().split())

stack = []
prev = '-'
result = 0
tmpVal = 0


for s in line:
    if s == '(' or s == '[':
        stack.append(s)
    elif s == ')':
        if prev == '(':

    prev = s