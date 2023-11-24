import copy
n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
INF = int(1e9)

mode = [
    [],
    [[0],[1],[2],[3]],
    [[0,2],[1,3]],
    [[0,1],[1,2],[2,3],[0,3]],
    [[0,1,2],[0,1,3],[1,2,3],[0,2,3]],
    [[0,1,2,3]]
]

# 북-동-남-서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

# [감시종류,행,열]
cctv = []
# cctv 위치 따기
for i in range(n):
    for j in range(m):
        if board[i][j] in [1,2,3,4,5]:
            cctv.append([board[i][j],i,j])

def dfs(depth,board):
    global min_val
    if depth == len(cctv):
        min_val = min(min_val,count(board))
    else:
        copy_board = copy.deepcopy(board)
        type,x,y = cctv[depth]
        for dir in mode[type]:
            watch(x,y,dir,copy_board)
            dfs(depth+1,copy_board)
            # 90도 회전하면서 재탐색
            copy_board = copy.deepcopy(board)

# 행,열,방향,복사 board
def watch(x,y,dir,board):
    for k in dir:
        nx,ny = x,y
        while True:
            nx += dx[k]
            ny += dy[k]
            if 0<=nx<n and 0<=ny<m:
                if board[nx][ny] == 6:
                    break
                elif board[nx][ny] == 0:
                    board[nx][ny] = '#'
            else:
                break

def count(board):
    cnt = 0
    for i in range(n):
        cnt += board[i].count(0)
    return cnt

min_val = INF
dfs(0,board)
print(min_val)