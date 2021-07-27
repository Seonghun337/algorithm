n = 5
m = 6
nums = [list(map(int,input().split())) for _ in range(n)]

dxdys = [(1,0),(-1,0),(0,1),(0,-1)]
res = {}


def search(y,x,arr=[],k=0):
    if k == m:
        res[' '.join(list(map(str,arr)))] = 1
        return
    
    if len(arr) == 0:
        arr.append(nums[y][x])

    for dxdy in dxdys:
        dx,dy = dxdy
        nx,ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < n:
            arr.append(nums[ny][nx])
            search(ny,nx,arr,k+1)
            arr.pop()


for i in range(n):
    for j in range(n):
        search(i,j)

print(len(res))
