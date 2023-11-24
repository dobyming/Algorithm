import sys
input = sys.stdin.readline
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(i,j):
    global tmp
    queue.append([i,j])

    while queue:
        x,y = queue.popleft()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if board[nx][ny] == 1:
                    continue
                elif board[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx,ny])
                elif board[nx][ny] == 3 or board[nx][ny] ==4 or board[nx][ny] == 5:
                    visited[nx][ny] = visited[x][y] + 1
                    tmp.append([board[nx][ny],visited[nx][ny]])
                    break

n,m = map(int,input().split())
board = [list(map(int,input().rstrip())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
queue = deque([])
tmp = []

for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            bfs(i,j)

# tmp[0]: 음식종류, tmp[1]: 거리 측정
tmp.sort(key=lambda x:(x[1],x[0]))

if len(tmp) == 0:
    print("NIE")
else:
    print("TAK",end=" ")
    print()
    print(tmp[0][1])