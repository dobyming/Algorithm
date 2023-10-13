import sys
from collections import Counter,defaultdict
input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
    N = int(input().rstrip()) # 참가자 수 
    arr = list(map(int,input().split()))
    
    # 팀별 점수 계산
    team_score = defaultdict(list)
    for j in arr:
        if j not in team_score:
            team_score[j].append(0)
        else:
            continue

    # 각 팀 몇명 계산
    team_dict = Counter(arr)
    point = [0] * N # 점수 누적

    # 점수판 만들기
    score = 0
    for i in range(N):
        if team_dict[arr[i]] >= 6:
            point[i] =  score + 1
            team_score[arr[i]].append(point[i])
            score += 1
        else:
            continue
    
    winner = 0
    win_score = int(1e9)
    for team,arr in team_score.items():
        if len(arr) > 1:
            tmp_score = sum(arr[1:5])
            if tmp_score < win_score:
                winner = team
                win_score = tmp_score
            elif tmp_score == win_score:
                if team_score[winner][5] > team_score[team][5]:
                    winner = team
                    win_score = tmp_score
        else:
            pass

    print(winner)