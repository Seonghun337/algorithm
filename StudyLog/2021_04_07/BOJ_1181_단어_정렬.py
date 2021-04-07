#2020-04-07
import sys
def main():
    n = int(input())
    words = []
    for _ in range(n):
        line = sys.stdin.readline().rstrip()
        words.append((len(line),line))

    words.sort()
    prev = ''
    for word in words:
        if prev != word[1]:
            print(word[1])
        prev = word[1]

    
main()