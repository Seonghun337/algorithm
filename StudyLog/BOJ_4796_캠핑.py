#2021-04-07

def solution(L,P,V):
    result = (V//P)*L
    result = result + min(V%P,L)
    return result

def main():
    inputs = []
    while 1:
        L,P,V = map(int,input().split())
        if L == 0 and P == 0 and V == 0:
            break
        else:
            inputs.append((L,P,V))

    for i in range(len(inputs)):
        L,P,V = inputs[i]
        print('Case ' + str(i+1) + ': ' + str(solution(L,P,V)))



main()