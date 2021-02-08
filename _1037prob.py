


def solve(divisors):
    divisors.sort()
    if len(divisors) == 1:
        return pow(divisors[0],2)
    else:
        return divisors[0]*divisors[-1]

def main():
    n = int(input())
    divisors = list(map(int,input().split(' ')))

    print(solve(divisors))
        


main()