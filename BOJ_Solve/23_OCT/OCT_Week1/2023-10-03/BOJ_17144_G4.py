import sys
input = sys.stdin.readline

r,c,t = map(int,input().split())
# -1로 기록된 부분이 공기 청정기 위치
board = [list(map(int,input().split())) for _ in range(r)]

up,down = 0,0
for i in range(r):
    if board[i][0] == -1:
        up = i
        down = i+1
        break

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dust():
    tmp_arr = [[0]*c for _ in range(r)] #여기에 저장
    for i in range(r):
        for j in range(c):
            if board[i][j] != -1 or board[i][j] == 0:
                tmp = 0 # 확산되는 양
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0<=nx<r and 0<=ny<c and board[nx][ny] != -1:
                        tmp_arr[nx][ny] += board[i][j] // 5
                        tmp += board[i][j] // 5 # 남는양 방향별로 누적
                board[i][j] -= tmp # 남은 미세먼지의 양
    
    # 갱신
    for i in range(r):
        for j in range(c):
            board[i][j] += tmp_arr[i][j]

# 공기청정기 확산(반시계 방향으로 옮겨야함)
def s_up():
   # 동북서남
   dx = [0,-1,0,1]
   dy = [1,0,-1,0] 
   d,before = 0,0
   x,y = up,1

   while True:
       nx = x+dx[d]
       ny = y+dy[d]
       if x == up and y == 0:
           break
       if nx < 0 or nx >= r or ny < 0 or ny >= c:
           d += 1
           continue
       board[x][y],before = before,board[x][y]
       x,y = nx,ny

def s_down():
    # 동남서북
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    d,before = 0,0
    x,y = down,1

    while True:
        nx = x+dx[d]
        ny = y+dy[d]
        if x == down and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            d += 1
            continue
        board[x][y], before = before,board[x][y]
        x,y = nx,ny


for _ in range(t):
    dust()
    s_up()
    s_down()

answer = 0
for i in range(r):
    for j in range(c):
        if board[i][j] >0:
            answer += board[i][j]

print(answer)