# 울타리 영역 안의 양들의 숫자 > 늑대의 숫자: 늑대가 전부 먹힘
# 양들의 숫자 <= 늑대의 숫자 : 양이 전부 먹힘 
# 몇마리의 양과 늑대가 살아남을 수 있을지 return 
# 동서남북으로만 이동 가능
# v: 늑대, k:양

import sys
input = sys.stdin.readline
from collections import deque

def bfs(i,j):
    queue.append([i,j])
    visited[i][j] = True
    v_cnt,k_cnt = 0,0

    while queue:
        x,y = queue.popleft()
        if board[x][y] == 'v':
            v_cnt += 1
        elif board[x][y] == 'k':
            k_cnt += 1
        # '.'
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<R and 0<=ny<C and not visited[nx][ny]:
                if board[nx][ny] != '#':
                    queue.append([nx,ny])
                    visited[nx][ny] = True
    
    if v_cnt >= k_cnt:
        k_cnt = 0
    elif v_cnt < k_cnt:
        v_cnt = 0

    return v_cnt,k_cnt

R,C = map(int,input().split())
board = [list(input().rstrip()) for _ in range(R)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[False]*C for _ in range(R)]
queue = deque([])
v,k = 0,0

for i in range(R):
    for j in range(C):
        if board[i][j] != '#' and not visited[i][j]:
            v_cnt,k_cnt = bfs(i,j)
            v+=v_cnt
            k+=k_cnt

print(k,v)