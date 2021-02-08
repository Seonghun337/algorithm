def solve(inputRow):
    x1,y1,r1,x2,y2,r2 = inputRow

    if (x1,y1) == (x2,y2):
        if r1 == r2:
            return -1
        else:
            return 0
    else:
        d = getDistance(x1,y1,x2,y2)
        if abs(r1-r2) < d and d < r1 + r2:
            return 2
        elif abs(r1-r2) == d or d == r1 + r2:
            return 1
        else:
            return 0

def getDistance(x1,y1,x2,y2):
    return (((x1-x2) ** 2) + ((y1-y2) ** 2)) ** 0.5

def main():
    T = int(input())
    inputList = []
    for i in range(T):
        inputList.append(list(map(int,input().split(' '))))
    for inputRow in inputList:
        print(solve(inputRow))

main()