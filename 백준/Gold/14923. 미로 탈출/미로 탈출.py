import sys
input = sys.stdin.readline
from collections import deque

# 시작과 탈출 위치가 주어짐 
# 벽을 길로 만들 수 있음 지팡이로
# 지팡이는 단 한번만 사용할 수 있다.(벽 부술때는 시간 계산x) 
# 미로 탈출 여부 return, 가장 빠른 D를 return 
# 탈출 못하면 -1 출력

n,m = map(int,input().split())
hx,hy = map(int,input().split()) # 시작 위치
ex,ey = map(int,input().split()) # 도착 위치 
board = [list(map(int,input().split())) for _ in range(n)]

answer = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]

queue = deque([])
visited = [[[False for _ in range(2)] for _ in range(m)] for _ in range(n)]

def bfs(i,j):
    # 0: 시간 , 1: 지팡이
    queue.append([i,j,0,1])
    # 초기 지팡이1개로 시작 1번 idx에 박아두기
    visited[i][j][1] = True

    while queue:
        x,y,cnt,magic = queue.popleft()
        if x == ex-1 and y == ey-1:
            return cnt
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny][magic]:
                    continue
                elif board[nx][ny] == 0:
                    queue.append([nx,ny,cnt+1,magic])
                    visited[nx][ny][magic] = True
                elif board[nx][ny] == 1 and magic == 1:
                    visited[nx][ny][0] = True
                    queue.append([nx,ny,cnt+1,magic-1])
                
    return -1
    
print(bfs(hx-1,hy-1))