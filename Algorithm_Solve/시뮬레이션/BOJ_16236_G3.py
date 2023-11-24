import sys 
input = sys.stdin.readline
from collections import deque

n = int(input().rstrip())
# 0:빈칸, 9: 아기상어 위치, 나머지 수: 칸에 있는 물고기의 크기 
board = [list(map(int,input().split())) for _ in range(n)]

# 현재 아기상어의 위치
cx,cy = 0,0
# 아기상어의 크기,물고기 먹은 수
baby_shark,eat_fish = 2,0

for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            board[i][j] = 0
            cx,cy = i,j

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(i,j):
    global baby_shark
    time = [[0]*n for _ in range(n)]
    visited = [[False]*n for _ in range(n)]

    queue = deque([])
    queue.append([i,j])
    visited[i][j] = True

    # 물고기 값,행,열 : 행 오름차순 => 열 오름차순
    mul_fish = []
    
    while queue:
        x,y = queue.popleft()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if board[nx][ny] <= baby_shark:
                    time[nx][ny] = time[x][y] + 1
                    visited[nx][ny] = True
                    queue.append([nx,ny])

                    if board[nx][ny] < baby_shark and board[nx][ny] != 0:
                        # 행,열,시간순(거리가 짧=시간 짧)
                        mul_fish.append([nx,ny,time[nx][ny]])
    
    mul_fish.sort(key=lambda x:(x[2],x[0],x[1]))
    
    return mul_fish

answer = 0
while True:
    tmp_arr = bfs(cx,cy)
    
    if len(tmp_arr) == 0:
        print(answer)
        exit(0)
    
    # 거리가 가깝고,위에서 왼쪽 
    cx,cy,st = tmp_arr[0]
    
    eat_fish += 1
    if baby_shark == eat_fish:
        baby_shark += 1
        eat_fish = 0
    
    # 방문시, 빈칸으로 만든다. 
    board[cx][cy] = 0
    answer += st