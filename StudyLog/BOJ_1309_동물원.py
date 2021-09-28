import sys
n = int(sys.stdin.readline().rstrip())
#i번째에 있는 것만 침
f = 0
f_prev = 2
g = 1

if n == 1:
    print(3)
else:
    for i in range(2,n+1):
        f = g*2 + f_prev
        g = g + f_prev
        f_prev = f

    g = g + f

    print(g % 9901)