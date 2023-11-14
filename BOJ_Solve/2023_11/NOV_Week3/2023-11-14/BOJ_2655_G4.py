from collections import deque

n = int(input())
board = [list(input()) for _ in range(n)]

dx = [-1,1,0,0]
dy= [0,0,-1,1]
queue = deque([])

def bfs(i,j):
    visited = [[-1]*n for _ in range(n)]
    queue.append([i,j])
    visited[i][j] = 0

    while queue:
        x,y = queue.popleft()
        if x == n-1 and y==n-1:
            return visited[x][y]
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == -1:
                if board[nx][ny] == '1':
                    queue.appendleft([nx,ny])
                    visited[nx][ny] = visited[x][y]
                else:
                    queue.append([nx,ny])
                    visited[nx][ny] = visited[x][y] + 1

print(bfs(0,0))