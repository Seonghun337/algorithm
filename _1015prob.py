
def solve(lst):
    result = []
    slst = sorted(lst)
    
    for i in lst:
        j = slst.index(i)
        slst[j] = -1
        result.append(j)
    return result

def main():
    T = int(input())
    inputRow = list(map(int,input().split(' ')))
    print((' ').join(list(map(str,solve(inputRow)))))

main()
