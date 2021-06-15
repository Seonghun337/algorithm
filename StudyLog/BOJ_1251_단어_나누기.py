#2021-04-07

def main():
    word = input()
    l = len(word)

    Min = 'z'*51

    for i in range(1,l-1):
        for j in range(i+1,l):
                
                head = list(word[0:i])
                body = list(word[i:j])
                tail = list(word[j:l])

                head.reverse()
                body.reverse()
                tail.reverse()

                newWord = (''.join(head) + ''.join(body) + ''.join(tail))
                Min = min(Min, newWord)

    print(Min)

main()
