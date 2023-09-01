import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

def dfs(x,y):
    if x == n-1 and y == m-1:
        return 1
    
    if dp[x][y] == -1:
        dp[x][y] = 0
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if 0<=nx<n and 0<=ny<m:
                if board[x][y] > board[nx][ny]:
                    dp[x][y] += dfs(nx,ny)
    return dp[x][y]

n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

# 갈 수 있는 경로의 가짓수를 dp 2차원 배열로 기록
dp = [[-1]*m for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

print(dfs(0,0))