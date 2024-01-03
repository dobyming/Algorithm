import sys
from collections import deque

def solution(land):
    answer = 0
    # 각 석유 덩어리에서 발견된 부분의 뭉텅이를 열마다 기록한다. 
    N = len(land)
    M = len(land[0])
    queue = deque([])
    
    visited = [[False]*M for _ in range(N)]
    result = [0 for _ in range(M)] # 각 열별로 얻을 수 있는 양 
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    def bfs(i,j):
        queue.append([i,j])
        visited[i][j] = True
        cnt = 0
        sY,eY = sys.maxsize , -sys.maxsize
        
        while queue:
            x,y = queue.popleft()
            cnt += 1
            sY = min(sY,y)
            eY = max(eY,y)
            
            for k in range(4):
                nx = x+dx[k]
                ny = y+dy[k]
                if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
                    if land[nx][ny] == 1:
                        visited[nx][ny] = True
                        queue.append([nx,ny])
            
        for col in range(sY,eY+1):
            result[col] += cnt
        
    
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and land[i][j] == 1:
                bfs(i,j)

    answer = max(result)
    
    return answer