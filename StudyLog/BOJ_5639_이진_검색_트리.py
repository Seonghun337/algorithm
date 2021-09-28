from collections import defaultdict
import sys 
nodes = []

while True:
    try:
        node = int(input())
    except:
        break

    nodes.append(node)

n = len(nodes)
sys.setrecursionlimit(100002)

def search(start=0, end=n):
    if start>=end:
        return
    
    if end-start == 1:
        print(nodes[start])
        return

    target = nodes[start]
    a = start+1
    b = end
    while a < b:
        mid = (a + b) // 2

        if nodes[mid] > target:
            b = mid
        else:
            a = mid + 1

    search(start+1,b)
    search(b,end)
    print(nodes[start])

# print(nodes)
search()