# # a of b

# def getLCM(a,b):
#     return a * b // getGCD(a,b)


def getGCD(a,b):
    while b!=0:
        r = a % b
        a = b
        b = r
    return a


a1,b1 = map(int, input().split())
a2,b2 = map(int, input().split())

a3 = a1*b2 + a2*b1
b3 = b1 * b2

while 1:
    gcd = getGCD(a3,b3)
    if gcd == 1:
        break
    else:
        a3 = a3 // gcd
        b3 = b3 // gcd

print(a3,b3)