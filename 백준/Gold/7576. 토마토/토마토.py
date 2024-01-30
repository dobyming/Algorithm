# 창고에 보관된 토마토들이 며칠이 지나야 다 익는지 알고 싶음
# 1: 익은 토마토, 0: 익지 않은 토마토, -1: 빈공간
from collections import deque

def bfs():
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<n and 0<=ny<m and tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[x][y] + 1
                queue.append([nx,ny])
    return tomato
        

m,n = map(int,input().split())
tomato = [list(map(int,input().split())) for _ in range(n)]
queue = deque([])

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            queue.append([i,j])

bfs()
answer = 0
for tom in tomato:
    for t in tom:
        if t == 0:
            print(-1)
            exit(0)
    answer = max(answer,max(tom))

print(answer-1)