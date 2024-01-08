import sys
input = sys.stdin.readline
from collections import deque

m,n = map(int,input().split())
cheeze = [list(map(int,input().split())) for _ in range(m)]

queue = deque([])
dx = [-1,1,0,0]
dy = [0,0,-1,1]

time = 1 # 다 없어지는데 걸리는 시간 
cnt = 0 # 치즈 개수

for i in range(m):
    cnt += sum(cheeze[i])

def bfs():
    queue.append([0,0])
    melt = deque([])
    while queue:
        x,y = queue.popleft()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<m and 0<=ny<n and not visited[nx][ny]:
                if cheeze[nx][ny] == 0:
                    queue.append([nx,ny])
                elif cheeze[nx][ny] == 1:
                    melt.append([nx,ny])
                visited[nx][ny] = True
    
    # 녹은칸으로 만들기
    for mx,my in melt:
        cheeze[mx][my] = 0
        
    return len(melt)

# 치즈칸이 모두 사라질때 까지
while True:
    visited = [[False]*n for _ in range(m)]
    melt_cnt = bfs()
    cnt -= melt_cnt
    if cnt == 0:
        print(time)
        print(melt_cnt)
        break
    time += 1