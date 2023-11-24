import sys
input = sys.stdin.readline
from itertools import combinations
from collections import deque

# 행,열,초록,빨강
n,m,g,r = map(int,input().split())
# 0:호수, 1:배양액이 퍼지긴함, 2: 배양액이 자리 잡을 수 있는 땅
board = [list(map(int,input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(green,red,board):
    cnt = 0
    visited = [[0]*m for _ in range(n)]
    queue = deque([])

    # 초록색이면 -1로 
    for g in green:
        queue.append([g[0],g[1],'G'])
        visited[g[0]][g[1]] = -1
    # 빨간색이면 1로
    for r in red:
        queue.append([r[0],r[1],'R'])
        visited[r[0]][r[1]] = 1
    
    while queue:
        x,y,color = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and (board[nx][ny] ==1 or board[nx][ny] == 2) and visited[nx][ny] != 'F' and visited[nx][ny] == 0 and visited[nx][ny] < 999999:
                # 만약 초록색이라면 주변은 -1로 변함
                if visited[x][y] < 0:
                    visited[nx][ny] = visited[x][y] - 1
                    queue.append([nx,ny,color])
                # 만약 빨간색이라면 주변은 2로 변함
                elif 0<visited[x][y]<999999:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx,ny,color])
            
            # 초록색과 빨간색이 만나면 0이 되고 꽃이 생기는 지점임 
            if 0<=nx<n and 0<=ny<m and board[nx][ny] != 0 and visited[nx][ny] + visited[x][y] + 1 == 0:
                visited[nx][ny] = 999999
                cnt += 1
    return cnt

locs = []
# 2인 곳의 위치 값을 먼저 뽑고, 거기에 배양액을 뿌릴 수 있는 가짓수
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            locs.append((i,j))

# 초록색 배치 후, 남은거 빨간색에다가 주는 idea
# 차집합 연산을 위해 set으로 변환
ls = set(locs)
answer = 0
for green in combinations(locs,g):
    g_residue = list(ls-set(green))
    g_locs = list(green) # 초록색 위치
    for red in combinations(g_residue,r):
        r_locs = list(red) # 빨간색 위치
        tmp = bfs(g_locs,r_locs,board)
        answer = max(answer,tmp)

print(answer)