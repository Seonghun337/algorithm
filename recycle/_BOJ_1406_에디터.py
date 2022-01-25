line = list(input())
n = int(input())

commands = []
cursor = len(line)

for _ in range(n):
    i = input()
    commands.append(i)

for command in commands:
    if command == 'L':
        if cursor-1 >= 0:
            cursor = cursor - 1
    elif command == 'D':
        if cursor+1 <= len(line):
            cursor = cursor + 1
    elif command == 'B':
        if cursor-1 >= 0:
            cursor = cursor-1
            del line[cursor]
    else:
        c, p = command.split()
        if c == 'P':
            line.insert(cursor,p)
            cursor = cursor - 1


print(str(line))