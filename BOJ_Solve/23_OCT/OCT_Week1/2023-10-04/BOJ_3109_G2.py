import sys
input = sys.stdin.readline

R,C = map(int,input().split())
board = [list(input().rstrip()) for _ in range(R)]

visited = [[False]*C for _ in range(R)]
cnt = 0

dx = [-1, 0, 1]
dy = [1, 1, 1]

def bfs(i,j):
    global cnt
    visited[i][j] = True

    if j == C-1:
        cnt += 1
        return True

    for k in range(3):
        nx = i+dx[k]
        ny = j+dy[k]
        if 0<=nx<R and 0<=ny<C:
            if board[nx][ny] != 'x' and not visited[nx][ny]:
                if bfs(nx,ny):
                    return True
    
for i in range(R):
    bfs(i,0)

print(cnt)