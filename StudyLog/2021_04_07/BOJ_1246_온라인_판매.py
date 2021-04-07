#2021-04-07

def main():
    n,m = map(int,input().split())
    customers = []
    for _ in range(m):
        customers.append(int(input()))

    customers.sort(reverse=True)

    Max = -1
    MaxPrice = -1
    cnt = 0
    for customer in customers:
        if cnt < n:
            cnt = cnt + 1
        if Max < (cnt * customer):
            Max = cnt * customer
            MaxPrice = customer

    print(MaxPrice,Max)

main()