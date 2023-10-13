import sys
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    n,k,t,m = map(int,input().split())
    # 각 팀에 대해서 문제별 획득 점수 
    score = [[0]*k for _ in range(n)]
    cnt = [0] * n # 제출 횟수
    time = [0] * n
    
    for t_cnt in range(m):
        # 팀 id, 문제 번호, 획득한 점수 
        i,j,s = map(int,input().split())
        if score[i-1][j-1] < s:
            score[i-1][j-1] = s
        cnt[i-1] += 1
        time[i-1] = t_cnt    
    
    # [각 팀점수,제출횟수,제출시간]
    new_score = []
    for l in range(n):
        new_score.append([sum(score[l]),cnt[l],time[l],l+1])
    
    new_score.sort(key=lambda x:(-x[0],x[1],x[2]))
    for i in range(len(new_score)):
        if new_score[i][3] == t:
            print(i+1)
            break