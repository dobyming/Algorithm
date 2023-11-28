# 검은색: 전류 차단, 흰색: 전류가 통함 
# 전류는 섬유 물질의 가장 바깥쪽 흰색 격자들에게 동서남북으로 제공
# 즉 0행에서 출발해서 아래행까지 도달할 수 있는지 여부 return 

import sys
input = sys.stdin.readline
from collections import deque

m,n = map(int,input().split())
# 0: 흰색, 1: 검은색
board = [list(input().rstrip()) for _ in range(m)]
visited = [[False]*n for _ in range(m)]
queue = deque([])

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(i,j):
    queue.append([i,j])
    visited[i][j] = True

    while queue:
        x,y = queue.popleft()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<m and 0<=ny<n and not visited[nx][ny]:
                if board[nx][ny] == '0':
                    queue.append([nx,ny])
                    visited[nx][ny] = True


for j in range(n):
    if board[0][j] == '0' and not visited[0][j]:
        bfs(0,j)

if True in visited[-1]:
    print("YES")
else:
    print("NO")