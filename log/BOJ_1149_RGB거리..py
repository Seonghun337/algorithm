n = int(input())

colors = [list(map(int,input().split())) for _ in range(n)]

for i in range(1,len(colors)):
    for j in range(3):
        colors[i][j] = min(colors[i-1][(j+1)%3],colors[i-1][(j+2)%3]) + colors[i][j]
print(min(colors[-1]))