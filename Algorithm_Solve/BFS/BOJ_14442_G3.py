import sys
from collections import deque
input = sys.stdin.readline

n,m,k = map(int,input().split())
board = [list(map(int,input().rstrip())) for _ in range(n)]
visited = [[[0]*(k+1) for _ in range(m)] for _ in range(n)]
queue = deque()

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    queue.append([0,0,k])
    visited[0][0][k] = 1 
    while queue:
        x,y,z = queue.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][z]
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if board[nx][ny] == 0 and visited[nx][ny][z] == 0:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    queue.append([nx,ny,z])
                # 벽이고 부시기 가능
                elif board[nx][ny] == 1 and z>0 and visited[nx][ny][z-1] == 0:
                    # 벽 부실때마다 하나씩 z개의 벽을 차감해야 함
                    visited[nx][ny][z-1] = visited[x][y][z] + 1
                    queue.append([nx,ny,z-1])
    return -1 

print(bfs())