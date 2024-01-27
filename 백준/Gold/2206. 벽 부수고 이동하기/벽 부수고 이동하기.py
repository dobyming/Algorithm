import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
board = [list(map(int,list(input().rstrip()))) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[[False]*2 for _ in range(m)] for _ in range(n)]

queue = deque([])

def bfs(i,j):
    queue.append([i,j,1,1])
    visited[i][j][1] = True

    while queue:
        x,y,cnt,result = queue.popleft()
        if x == n-1 and y == m-1:
            return result
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny][cnt]:
                    continue
                elif board[nx][ny] == 0:
                    visited[nx][ny][cnt] = True
                    queue.append([nx,ny,cnt,result+1])
                elif board[nx][ny] == 1 and cnt == 1:
                    visited[nx][ny][cnt-1] = 0
                    queue.append([nx,ny,cnt-1,result+1])
    
    return -1

print(bfs(0,0))