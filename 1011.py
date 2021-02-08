def solution(x,y):
    


def main():
    T = int(input())
    answers = []
    for _ in range(T):
        x,y = map(int,input().split())
        answers.append(solution(x,y))
    
    for answer in answers:
        print(answer)

main()