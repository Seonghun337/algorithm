n = int(input())

digits = [[0,1,1,1,1,1,1,1,1,1]]

for i in range(1,n):
    new = []
    for j in range(len(digits[0])):
        if j == 0:
            new.append(digits[i-1][1])
        elif j == 9:
            new.append(digits[i-1][8])
        else:
            new.append((digits[i-1][j-1]+digits[i-1][j+1]))

    digits.append(new)

# print(digits)
print(sum(digits[-1]) % int(1e9))