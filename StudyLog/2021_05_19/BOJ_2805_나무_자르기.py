import sys
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
trees = list(map(int,input().rstrip().split()))

def getSumOfCutted(h, trees):
    sum_ = 0
    for tree in trees:
        if tree - h > 0:
            sum_ = sum_ + tree - h
        else:
            continue

    return sum_

def search(a,b,m,trees):#log m
    mid = (a+b)//2

    sum_ = getSumOfCutted(mid, trees)

    if a==mid:
        return mid

    if sum_ < m:
        return search(a,mid,m,trees)
    else:
        return search(mid,b,m,trees)

print(search(0,int(1e9),m,trees))