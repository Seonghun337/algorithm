import sys

n = int(input())
triangle = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

for i in range(1,len(triangle)):
    for j in range(len(triangle[i])):
        if j==0 :
            triangle[i][j] = triangle[i][j] + triangle[i-1][j]
        elif j==len(triangle[i])-1:
            triangle[i][j] = triangle[i][j] + triangle[i-1][j-1]
        else:
            triangle[i][j] = triangle[i][j] + max(triangle[i-1][j],triangle[i-1][j-1])

print(max(triangle[-1]))