import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def burn():
    for _ in range(len(fire)):
        x,y = fire.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<h and 0<=ny<w:
                if board[nx][ny] == '.':
                    board[nx][ny] = '*'
                    fire.append((nx,ny))

def bfs():
    flag = False
    for _ in range(len(start)):
        x,y = start.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<h and 0<=ny<w:
                if visited[nx][ny] == 0 and board[nx][ny] == '.':
                    flag = True
                    visited[nx][ny] = visited[x][y] + 1
                    start.append((nx,ny))
            else:
                return visited[x][y]
    if not flag:
        return 'IMPOSSIBLE'

T = int(input().rstrip())
for _ in range(T):
    # w: 열 h: 행
    w,h = map(int,input().split())
    board = [list(input().rstrip()) for _ in range(h)]
    visited = [[0]*w for _ in range(h)]

    fire = deque([])
    start = deque([])

    for i in range(h):
        for j in range(w):
            if board[i][j] == '*':
                fire.append((i,j))
            if board[i][j] == '@':
                start.append((i,j))
    
    visited[start[0][0]][start[0][1]] = 1
    
    answer = 0
    while True:
        burn()
        answer = bfs()
        if answer:
            break
    
    print(answer)