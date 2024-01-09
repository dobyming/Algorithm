# 고슴도치는 비버의 굴로 가능한 빨리 도망가 홍수를 피하고자 함 
# 비버의 굴은 'D'로 표시, 고슴도치 위치는 'S'
# 매 분마다 고슴도치하는 인접하네 네칸중 한칸으로 이동할 수 있다. 

# 물이 있는 칸과 인접한 빈칸에는 물이 찬다. 
# 돌 통과 못하는거: 물, 고슴도치 
# 비버굴 통과 못하는거: 물
# 물 통과 못하는거: 고슴도치

# 고슴도치가 비버굴까지 가기 위한 최소 시간 return 

import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
board = [list(input().rstrip()) for _ in range(n)]

visited = [[0]*m for _ in range(n)]

queue = deque([])
dx = [-1,1,0,0]
dy = [0,0,-1,1] 

def bfs(Dx,Dy):
    while queue:
        x,y = queue.popleft()
        if board[Dx][Dy] == 'S':
            return visited[Dx][Dy]
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<n and 0<=ny<m:
                if (board[nx][ny] == '.' or board[nx][ny] == 'D') and board[x][y] == 'S':
                    board[nx][ny] = 'S'
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx,ny])
                # 고슴도치가 물로 차있는 곳을 못간다 = 고슴도치가 방문한 곳을 물로 뒤덮을 수 있다. 
                elif (board[nx][ny] == '.' or board[nx][ny] == 'S') and board[x][y] == '*':
                    board[nx][ny] = '*'
                    queue.append([nx,ny])
    
    return 'KAKTUS'

for i in range(n):
    for j in range(m):
        if board[i][j] == 'S':
            queue.append([i,j])
        elif board[i][j] == 'D':
            Dx,Dy = i,j
        
for i in range(n):
    for j in range(m):
        if board[i][j] == '*':
            queue.append([i,j])

print(bfs(Dx,Dy))