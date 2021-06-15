n = int(input())


def getGCD(a,b):
    while b!=0:
        r = a % b
        a = b
        b = r
    return a

def sol(first,target):
    while 1:
        gcd = getGCD(first,target)
        if gcd == 1:
            break
        else:
            first = first // gcd
            target = target // gcd
    print(str(first) + '/' + str(target))


inputs = list(map(int,input().split()))
for i in range(1,len(inputs)):
    sol(inputs[0], inputs[i])


