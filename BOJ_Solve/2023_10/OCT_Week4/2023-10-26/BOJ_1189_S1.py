import sys
input = sys.stdin.readline

R,C,K = map(int,input().split())
board = [list(input().rstrip()) for _ in range(R)]
answer = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(i,j,dist):
    global answer
    if dist == K and i == 0 and j == C-1:
        answer += 1
    else:
        # 방문처리
        board[i][j] = 'T'
        for k in range(4):
            nx = i+dx[k]
            ny = j+dy[k]
            if 0<=nx<R and 0<=ny<C and board[nx][ny] == '.':
                board[nx][ny] = 'T'
                dfs(nx,ny,dist+1)
                board[nx][ny] = '.'

dfs(R-1,0,1)
print(answer)