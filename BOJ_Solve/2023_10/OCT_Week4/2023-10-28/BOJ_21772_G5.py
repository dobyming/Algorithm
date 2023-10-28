import sys
input = sys.stdin.readline

R,C,T = map(int,input().split())
board = [list(input()) for _ in range(R)]

# 가희의 현재 위치 
gx,gy = 0,0
for i in range(R):
    for j in range(C):
        if board[i][j] == 'G':
            gx,gy = i,j

board[gx][gy] = '.'

# 최대로 먹고자하는 고구마의 수
g_eat = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(i,j,time,eat):
    global g_eat
    if time == T:
        g_eat = max(g_eat,eat)
        return
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0<=nx<R and 0<=ny<C:
            if board[nx][ny] == '#':
                continue
            elif board[nx][ny] == 'S':
                board[nx][ny] = '.'
                dfs(nx,ny,time+1,eat+1)
                board[nx][ny] = 'S'
            elif board[nx][ny] =='.':
                dfs(nx,ny,time+1,eat)

dfs(gx,gy,0,0)
print(g_eat)