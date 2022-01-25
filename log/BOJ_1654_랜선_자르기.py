import sys
k,n = map(int,input().split())

wires = [int(input()) for _ in range(k)]

# 길이 = L 이라고 하면, 길이 이진 탐색 시간 log(L)
# 각 길이마다 배열 탐색 (K)
# K log (L) ~= 30,000,000

def howManyWire(cut,wires):
    result = 0
    for wire in wires:
        result += (wire//cut)
    return result

def search(a,b,n,wires):
    mid = (a+b)//2
    
    nWire = howManyWire(mid,wires)

    if a==mid:
        return mid

    if nWire >= n:
        return search(mid,b,n,wires)
    else:
        return search(a,mid,n,wires)

print(search(0,sys.maxsize,n,wires))