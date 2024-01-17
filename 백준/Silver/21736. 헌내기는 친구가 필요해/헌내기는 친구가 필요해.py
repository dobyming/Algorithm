import sys
input = sys.stdin.readline
from collections import deque

def bfs(i,j):
    queue.append([i,j])
    visited[i][j] = True
    cnt = 0

    while queue:
        x,y = queue.popleft()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if board[nx][ny] == 'O':
                    queue.append([nx,ny])
                    visited[nx][ny] = True
                elif board[nx][ny] == 'P':
                    cnt += 1
                    queue.append([nx,ny])
                    visited[nx][ny] = True
                elif board[nx][ny] == 'X':
                    continue
    
    return cnt

n,m = map(int,input().split())
answer = 0
board = [list(input().rstrip()) for _ in range(n)]

visited = [[False]*m for _ in range(n)]
queue = deque([])
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(n):
    for j in range(m):
        if board[i][j] == 'I':
            cnt = bfs(i,j)
            answer += cnt

if answer == 0:
    print('TT')
else:
    print(answer)