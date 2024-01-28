import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
board = [list(input().rstrip()) for _ in range(m)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(i,j,color):
    queue = deque([])
    queue.append([i,j])
    cnt = 0
    board[i][j] = 0

    while queue:
        x,y = queue.popleft()
        cnt += 1
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<m and 0<=ny<n:
                if board[nx][ny] == color:
                    board[nx][ny] = 0
                    queue.append([nx,ny])
                else:
                    continue
    
    return cnt

w,b =0,0
for i in range(m):
    for j in range(n):
        if board[i][j] == 'W':
            w += (bfs(i,j,'W'))**2
        elif board[i][j] == 'B':
            b += (bfs(i,j,'B'))**2

print(w,b)