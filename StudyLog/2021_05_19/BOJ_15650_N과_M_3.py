n,m = map(int,input().split())

def func(n,m,k,set_):
    if m==k:
        print(' '.join(list(map(str,set_))))
        return
    else:
        for i in range(1,n+1):
            set_.append(i)
            func(n,m,k+1,set_)
            del set_[-1]

func(n,m,0,[])