import copy  
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    global answer
    tmp_board = copy.deepcopy(board)
    for i in range(n):
        for j in range(m):
            if tmp_board[i][j] == 2:
                queue.append((i,j))

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if tmp_board[nx][ny] == 0:
                    tmp_board[nx][ny] = 2
                    queue.append((nx,ny))
    # answer 
    cnt = 0
    for i in range(n):
        cnt += tmp_board[i].count(0)
    
    answer = max(answer,cnt)


def makeWall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                board[i][j] = 1
                makeWall(cnt+1)
                board[i][j] = 0

n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
queue = deque([])

answer = 0
makeWall(0)
print(answer)