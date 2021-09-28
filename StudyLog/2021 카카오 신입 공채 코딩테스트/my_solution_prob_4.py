# d = 사용한 화살의 개수
# def search(n,info,d=0):
# if d == n:

# 약간 배낭 문제 느낌
# 어피치가 점수를 못먹게 하면 점수차는 더 커진다

# '점수차'의 의미는, 비용 1로 먹으면 점수 만큼만 증가하고
# 어피치 비용+1로 먹으면 점수*2만큼 증가

# dp[x][i] = x발을 사용했을 때 i번째 과녁을 사용해서 얻을 수 있는 점수의 최댓값
# 점수를 보상,비용 오름차순으로 정렬 scores = (a,b) # a발 써서 b점 얻을 수 있음

import copy

def solution(n, info):

    
    score_apeach = 0
    for i in range(len(info)):
        if info[i] > 0:
            score_apeach += 10-i
    
    board_lion = [0 for _ in range(11)]
    print(score_apeach)
    search(n, info, board_lion, score_apeach)

    global answer,_max_gap
    if _max_gap == -1:
        return [-1]
    else:
        return answer

    
answer = []
_max_gap = -1


def search(n, board_apeach, board_lion, score_apeach, score_lion=0, idx=0, n_arrow_used=0):
    global _max_gap, answer
    
    if idx == 10:
        if n_arrow_used <= n:
            gap = score_lion - score_apeach
            if gap > 0 and gap > _max_gap:
                board_lion[-1] = n - n_arrow_used
                _max_gap = gap
                answer = copy.deepcopy(board_lion)
                print(board_lion, score_apeach, score_lion, gap)
            if gap == _max_gap and answer != []:
                for i in range(11):
                    if answer[10-i] < board_lion[10-i]:
                        board_lion[-1] = n - n_arrow_used
                        answer = copy.deepcopy(board_lion)
                    elif answer[10-i] == board_lion[10-i]:
                        continue
                    else:
                        break
            return
        else:
            return
    
    # idx번째를 라이언이 맞추는 경우
    score = 10 - idx
    # 어피치가 맞췄었던 경우
    if board_apeach[idx] > 0:
        n_need_arrow = board_apeach[idx] + 1
        board_lion[idx] = n_need_arrow
        search(n, board_apeach, board_lion, score_apeach-score, score_lion+score, idx+1, n_arrow_used+n_need_arrow)
    else:
        n_need_arrow = 1
        board_lion[idx] = n_need_arrow
        search(n, board_apeach, board_lion, score_apeach, score_lion+score, idx+1, n_arrow_used+n_need_arrow)
        
        
    # idx번째를 포기하는 경우
    board_lion[idx] = 0
    search(n, board_apeach, board_lion, score_apeach, score_lion, idx+1, n_arrow_used)