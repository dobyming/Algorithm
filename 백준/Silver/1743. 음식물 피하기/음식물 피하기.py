import sys
input = sys.stdin.readline
from collections import deque

def bfs(i,j):
    queue.append([i,j])
    visited[i][j] = True
    size = 1

    while queue:
        x,y = queue.popleft()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if board[nx][ny] == '#':
                    size += 1
                    queue.append([nx,ny])
                    visited[nx][ny] = True
                else:
                    continue
    
    return size

n,m,k = map(int,input().split())
answer = []
board = [['.']*m for _ in range(n)]
visited = [[False]*m for _ in range(n)]

for _ in range(k):
    a,b = map(int,input().split())
    board[a-1][b-1] = '#'

queue = deque([])
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(n):
    for j in range(m):
        if board[i][j] == '#':
            cnt = bfs(i,j)
            answer.append(cnt)

print(max(answer))