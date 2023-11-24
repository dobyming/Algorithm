import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations

n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
answer = int(1e9) # 최소 시간

# virus 위치 따기 
v_locs = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            v_locs.append([i,j])

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(locs):
    queue = deque(locs)
    visited = [[-1]*n for _ in range(n)]
    val = 0
    for a,b in queue:
        visited[a][b] = 0

    while queue:
        x,y = queue.popleft()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == -1:
                if board[nx][ny] != 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx,ny])
                    val = max(val,visited[x][y]+1)
    
    # 모든 빈칸에 퍼트릴 수 없을때
    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1 and board[i][j] != 1:
                return int(1e9)

    return val

# virus combinations
v_combs = list(combinations(v_locs,m))
for comb in v_combs:
    answer = min(answer,bfs(comb))

if answer == int(1e9):
    print(-1)
else:
    print(answer)