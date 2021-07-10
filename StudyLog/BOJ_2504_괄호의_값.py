
# def trans_prefix(brackets):
#     result = []
#     prev = '-'
#     stack = []
#     for s in brackets:
#         if s == '(' or s == '[':
#             stack.append(s)
#         if s == ')':
#             if prev == '(':
#                 result.append(2)
#                 stack.pop()
#             else:
#                 p = stack.pop()
#                 if p == '(':
#                     result.append(2)
#                     result.append('*')
#                     if prev == ')' or prev == ']':
#                         result.append('+')
#                 else:
#                     print("not possible")
#                     break
#         elif s == ']':
#             if prev == '[':
#                 result.append(3)
#                 stack.pop()
#             else:
#                 p = stack.pop()
#                 if p == '[':
#                     result.append(3)
#                     result.append('*')
#                     if prev == ')' or prev == ']':
#                         result.append('+')
#                 else:
#                     print("not possible")
#                     break
        
        
#         prev = s
    
#     return result

# def calc(prefix):
#     stack = []
#     for x in prefix:
#         if x == '*':
#             a = stack.pop()
#             b = stack.pop()
#             stack.append(a*b)
#         elif x == '+':
#             a = stack.pop()
#             b = stack.pop()
#             stack.append(a+b)
#         else:
#             stack.append(x)
    
#     return stack[0]

# print(trans_prefix(line))
# print(calc(trans_prefix(line)))
import sys

line = list(sys.stdin.readline().rstrip())

stack = []
isOk = 1
for x in line:
    if x == '(' or x == '[':
        stack.append(x)
    elif x == ')':
        tmp = []
        while 1:
            if not stack:
                isOk = 0
                break
            p = stack.pop()
            if p == '(':
                if tmp:
                    stack.append(sum(tmp)*2)
                else:
                    stack.append(2)
                break
            elif p == '[':
                isOk = 0
                break
            else:
                tmp.append(p)
    elif x == ']':
        tmp = []
        while 1:
            if not stack:
                isOk = 0
                break
            p = stack.pop()
            if p == '[':
                if tmp:
                    stack.append(sum(tmp)*3)
                else:
                    stack.append(3)
                break
            elif p == '(':
                isOk = 0
                break
            else:
                tmp.append(p)

try:
    result = sum(stack)
except:
    isOk = 0
    
if isOk:
    print(result)
else:
    print(0)
