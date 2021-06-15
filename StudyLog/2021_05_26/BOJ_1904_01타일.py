n = int(input())
prev = 1
pprev = 1
for i in range(2,n+1):
    tmp = (prev+pprev) % 15746
    prev = pprev
    pprev = tmp
print(pprev)