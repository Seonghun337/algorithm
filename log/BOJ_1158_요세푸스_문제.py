#2021-04-06

def solution(n,k):
    circle = [i+1 for i in range(n)]
    result = []
    
    i = -1
    while len(circle) > 0:
        i = (i + k) % len(circle)
        result.append(circle[i])
        del circle[i]
        i = i - 1

    return result

def main():
    n,k = map(int,input().split())
    print('<'+', '.join(map(str,solution(n,k)))+'>')

main()
