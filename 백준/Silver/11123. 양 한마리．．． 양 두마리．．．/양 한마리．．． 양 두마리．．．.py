import sys
input = sys.stdin.readline
from collections import deque

T = int(input().rstrip())
for _ in range(T):
    n,m = map(int,input().split())
    board = [list(input().rstrip()) for _ in range(n)]
    visited = [[False]*m for _ in range(n)]

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    queue = deque([])
    
    def bfs(i,j):
        queue.append([i,j])
        visited[i][j] = True
        while queue:
            x,y = queue.popleft()
            for k in range(4):
                nx = x+dx[k]
                ny = y+dy[k]
                if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                    if board[nx][ny] == '#':
                        queue.append([nx,ny])
                        visited[nx][ny] = True

    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == '#' and not visited[i][j]:
                bfs(i,j)
                cnt += 1

    print(cnt)