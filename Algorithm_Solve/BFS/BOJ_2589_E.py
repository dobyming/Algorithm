from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(i,j):
    queue.append((i,j))
    visited[i][j] = 1
    cnt = 0

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if board[nx][ny] == 'L' and not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    cnt = max(cnt,visited[nx][ny])
                    queue.append((nx,ny))
    
    return cnt-1

n,m = map(int,input().split())
board = [list(input()) for _ in range(n)]

queue = deque([])

result = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 'L':
            visited = [[0]*m for _ in range(n)]
            result = max(result,bfs(i,j))            

print(result)