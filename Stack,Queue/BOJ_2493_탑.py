import sys

def solution(n,tops):
    result = [0 for _ in range(n)]
    stack = []

    # stack.append((tops[0],0))
    for i in range(0,len(tops)):
        while stack:
            if stack[-1][0] > tops[i]:
                result[i] = stack[-1][1]+1
                break
            else:
                stack.pop()

        
        stack.append((tops[i],i))            

    return result


def main():
    n = int(input())
    tops = list(map(int,sys.stdin.readline().rstrip().split()))

    print(' '.join(map(str,solution(n,tops))))

main()