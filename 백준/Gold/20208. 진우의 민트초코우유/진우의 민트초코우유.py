import sys
input = sys.stdin.readline

def back_track(x,y,hp,mc):
    global cnt
    for nx,ny in mincho:
        if board[nx][ny] == 2:
            # 맨해튼 거리(최소값을 선택하자)
            dist = abs(x-nx) + abs(y-ny)
            if dist <= hp:
                board[nx][ny] = 0
                back_track(nx,ny,hp+H-dist,mc+1)
                board[nx][ny] = 2
    if abs(x-sx) + abs(y-sy) <= hp:
        cnt = max(cnt,mc)

N,M,H = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
mincho = []
sx,sy = 0,0

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            sx, sy = i,j
        elif board[i][j] == 2:
            mincho.append([i,j])

cnt = 0
# 집 위치좌표들,현제 체력,민초개수
back_track(sx,sy,M,0)
print(cnt)